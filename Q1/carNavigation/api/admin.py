from django.contrib import admin
from .models import Vehicle,NavigationRecord

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(NavigationRecord)