from django.contrib import admin
from django.urls import path, include

from .views import ProductListView, ProductDetailView, CommentCreateView, test_messages
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:pk>', CommentCreateView.as_view(), name='comment_create'),
    path('hello/', test_messages, name='test_messages'),
]
