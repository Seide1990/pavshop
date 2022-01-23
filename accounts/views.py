from django.shortcuts import render

# Create your views here.
from django.core.mail.message import sanitize_address
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . forms import RegistrationForm, LoginForm
from django.contrib import messages
from accounts.tasks import send_confirmation_mail
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from accounts.tools.tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login as django_login, logout as django_logout
User = get_user_model()


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password = form.cleaned_data.get('password1')
            user.is_active = False
            user.save()
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            send_confirmation_mail(user_id=user.id, site_address=site_address)
            messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
            return redirect(reverse_lazy('accounts:login'))
    context = {
        'form': form
    }

    return render(request, 'register.html', context)
# Create your views here.
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print('seide')
        if form.is_valid():
            print('delta')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user:
                print('davam')
                django_login(request, user)
                messages.success(request, 'Siz ugurla login oldunuz')
                mesaj_et='Siz login oldunuz'
                return redirect(reverse_lazy('home:index'),mesaj_et)
                
            else:
                print('yalnis')
                
                messages.success(request, 'Siz login ola bilmediniz')

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('home:index'))
    elif user:
        messages.error(request, 'Email is not activated.')
        return redirect(reverse_lazy('accounts:register'))
    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('accounts:register'))
@login_required
def logout(request):
    django_logout(request)
    
    return redirect(reverse_lazy('accounts:login'))