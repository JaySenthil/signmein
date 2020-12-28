from django.contrib import admin

# Register your models here.

from .models import Car, Driver

admin.site.register(Car)
admin.site.register(Driver)
