from django.db import models
from ckeditor.fields import RichTextField
from .choosen import PAYMENT_METHOD
from apps.common.models import BaseModel


class Contribute(BaseModel):
    full_name = models.CharField(max_length=100)
    support_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD)

    class Meta:
        verbose_name = 'Contribute'
        verbose_name_plural = 'Contributes'

    def __str__(self):
        return self.full_name


class Event(BaseModel):
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='events')
    location = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def views_count(self):
        return self.views + 1

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title


class UsefulLink(BaseModel):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='useful_links')
    link = models.URLField(max_length=200)

    class Meta:
        verbose_name = 'UsefulLink'
        verbose_name_plural = 'UsefulLinks'

    def __str__(self):
        return self.title
