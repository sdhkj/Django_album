from django.contrib import admin

# Register your models here.
# /photo/admin.py

from django.contrib import admin
from photo.models import Photo

admin.site.register(Photo)