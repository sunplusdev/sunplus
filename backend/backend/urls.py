from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/accounts/', include('accounts.urls')),
    ]
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/accounts/', include('accounts.urls')),
    ]
