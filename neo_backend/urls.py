# urls.py (principal)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('apps.users.urls')),
    path('api/users/', include('apps.users.api_urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/permissions/', include('permissions.urls')),
    path('api/settings/', include('settings.urls')),
    path('api/sites/', include('sites.urls')),
    path('api/energy/', include('energy_data.urls')),
    path('api/companies/', include('companies.urls')),
    path('api/alarms/', include('alarms.urls')),
    path('api/notifications/', include('notifications.urls')),

    path('api/', include('apps.core.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)