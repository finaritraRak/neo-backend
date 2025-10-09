# apps/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    login_view,
    logout_view,
    me_view,
    dashboard_stats,
    forgot_password,
    reset_password
)

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('me/', me_view, name='me'),
    path('stats/', dashboard_stats, name='dashboard-stats'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('reset-password/', reset_password, name='reset-password'),
    path('', include(router.urls)),
]