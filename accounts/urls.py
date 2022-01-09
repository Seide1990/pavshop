from django.urls import path, re_path
from .views import register ,activate
from accounts import views

app_name='accounts'
urlpatterns=[
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
    path('logout/',views.logout,name='logout'),

]
