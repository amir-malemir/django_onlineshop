from django.contrib import admin
from .models import Products, Comments


class CommentsInline(admin.TabularInline):
    model = Comments
    fields = ('author', 'body', 'stars', 'active')
    extra = 1


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'active', 'datetime_created', 'datetime_modified')
    inlines = [CommentsInline]


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'body', 'stars', 'active', 'datetime_created', 'datetime_modified')

