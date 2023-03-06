from django.db import models
import json
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount



class Management(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='managements')
    position = models.CharField(max_length=100)
    phone = PhoneNumberField()
    reception_days = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Management'
        verbose_name_plural = 'Managements'


class Representation(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='representations')
    icon_flag = models.ImageField(upload_to='representations')
    country = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Representation'
        verbose_name_plural = 'Representations'


class Career(models.Model):
    title = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='careers')
    country = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    type_work = models.CharField(max_length=100)
    description = models.TextField()
    requrements = RichTextField()
    views = models.ManyToManyField('hitcount.HitCount', related_name='hit_count_generic_relation', blank=True)

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Career'
        verbose_name_plural = 'Careers'


class SendCV(models.Model):
    work = models.ForeignKey(Career, on_delete=models.CASCADE)
    phone = PhoneNumberField()
    cv = models.FileField(upload_to='cv')

    def __str__(self):
        return self.work.title

    class Meta:
        verbose_name = 'Send CV'
        verbose_name_plural = 'Send CVs'




class Instagramlink(models.Model):
    image = models.ImageField()
    link = models.CharField(max_length=100)



    class MEta:
        verbose_name = 'Instagram Link'
        verbose_name_plural = 'Instagram Links'

    def __str__(self):
        return self.link