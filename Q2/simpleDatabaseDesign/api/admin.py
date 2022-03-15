from django.contrib import admin
from .models import Bin,Operation,Bin_Operation

# Register your models here.
admin.site.register(Bin)
admin.site.register(Operation)
admin.site.register(Bin_Operation)
