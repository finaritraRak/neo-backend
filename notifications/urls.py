# notifications/urls.py
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/', views.NotificationDetailView.as_view(), name='notification-detail'),
    path('<int:pk>/read/', views.MarkNotificationAsReadView.as_view(), name='notification-read'), 
    path('mark-all-read/', views.MarkAllNotificationsAsReadView.as_view(), name='mark-all-read'),
    path('unread-count/', views.unread_notifications_count, name='unread-count'),
    path('<int:pk>/delete/', views.DeleteNotificationView.as_view(), name='notification-delete'),
    path('delete-multiple/', views.DeleteMultipleNotificationsView.as_view(), name='notification-delete-multiple'),
]