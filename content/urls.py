# content/urls.py
from django.urls import path
from .views import page_content_list, page_content_detail, index

urlpatterns = [
    path('', index, name='content-index'),
    path('pages/', page_content_list, name='page-content-list'),
    path('pages/<int:pk>/', page_content_detail, name='page-content-detail'),
]
