from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users.views import signin_user, signout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signin/', signin_user, name='signin'),
    path('accounts/signout/', signout_user, name='signout'),
    path('', include('shortener.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
