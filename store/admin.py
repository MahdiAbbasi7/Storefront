from django.contrib import admin
from . import models

# admin.site.register(models.Product, ProductAdmin)
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status']
    list_editable = ['price']
    list_per_page = 15

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory_type < 10 : 
            return 'LOW'
        return 'OK'
    
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 15
    ordering = ['first_name', 'last_name']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 15
    ordering = ['title']