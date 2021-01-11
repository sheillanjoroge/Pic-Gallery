from django.contrib import admin

from .models import Tag, Location, Image

# Register your models here.
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Image)


