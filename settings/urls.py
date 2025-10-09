# settings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='settings-index'),
    path('site/', views.site_settings_view, name='site-settings'),
    path('api/user/profile/', views.user_profile_view, name='user-profile'),
]