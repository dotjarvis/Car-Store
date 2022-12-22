from django.contrib import admin
from . models import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ('brand','model','price','production_year' ,'transmission_mode','color','engine_capacity')

admin.site.register(Store,StoreAdmin)