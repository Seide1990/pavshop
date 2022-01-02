from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('product/', include('product.urls', namespace='product')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
