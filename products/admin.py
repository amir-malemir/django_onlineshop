from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'active', 'datetime_created', 'datetime_modified')
