from django.contrib import admin
from .models import Photo, Category, Location

# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Location)