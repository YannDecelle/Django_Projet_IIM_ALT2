from django.contrib import admin

from .models import ShopModel

class ShopAdmin(admin.ModelAdmin):
    fields=['Product_Name','Product_Description','Product_Stock','Product_Price']

admin.site.register(ShopModel)