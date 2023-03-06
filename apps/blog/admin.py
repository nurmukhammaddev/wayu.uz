from django.contrib import admin
from .models import Blog, Country, Category

# Register your models here.

admin.site.register(Blog)
admin.site.register(Country)
admin.site.register(Category)
