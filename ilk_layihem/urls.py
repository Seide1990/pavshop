from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns += i18n_patterns(
    path('contact/', include('contact.urls', namespace='contact')),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('home.urls', namespace='home')),
    #path('order/', include('order.urls', namespace='order')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('product/', include('product.urls', namespace='product')),
   )
