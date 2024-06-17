from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from django.shortcuts import reverse


class Products(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    # cover = models.ImageField(upload_to='')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comments(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect'))
    ]
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments',)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', )
    body = models.TextField(verbose_name=_('your comment: '))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('rate'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    # Manager
    objects = models.Manager()
    Active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
