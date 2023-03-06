from django.contrib import admin
from .models import Representation, Career, Management, Instagramlink

# Register your models here.

class INstagramlinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'link')
    list_display_links = ('id', 'image', 'link')
    search_fields = ('id', 'image', 'link')
    list_per_page = 15


admin.site.register(Representation)
admin.site.register(Career)
admin.site.register(Instagramlink, INstagramlinkAdmin)

admin.site.register(Management)