from django.contrib import admin
from django.apps import apps

from .models import  list_of_models


class ShopAdmin(admin.ModelAdmin):
    pass


for model in list_of_models:
    admin.site.register(model, ShopAdmin)
