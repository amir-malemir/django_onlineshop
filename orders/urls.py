from django.contrib import admin
from django.urls import path, include

from .views import order_create_view
from . import views

app_name = 'order'
urlpatterns = [
    path('create/', order_create_view, name='order_create'),

]
