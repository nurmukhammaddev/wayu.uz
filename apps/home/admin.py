from django.contrib import admin
from .models import Contribute, Event, UsefulLink
# Register your models here.

admin.site.register(Contribute)
admin.site.register(Event)
admin.site.register(UsefulLink)