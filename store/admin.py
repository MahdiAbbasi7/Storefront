from typing import Any
from django.contrib import admin, messages
from django.db.models import Count
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.html import format_html
from urllib.parse import urlencode
from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields=['tumbnail']

    def tumbnail(self, instance):
        if instance.image.name!='':
            return format_html(f'<img src="{instance.image.url}" class="tumbnail" />')
        return ''


# admin.site.register(models.Product, ProductAdmin)
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']
    autocomplete_fields=['collections']
    prepopulated_fields={
        'slug':['title'],
    }
    actions=['clear_inventory']
    inlines=[ProductImageInline]
    list_display = ['title', 'price', 
                    'inventory_status', 'collections',]
    list_editable = ['price']
    list_per_page = 15
    # for optimaize performance use select_related for increase queries.
    list_select_related = ['collections']
    list_filter = ['collections', 'last_updated', InventoryFilter]

    def collections(self, product):
        return product.collections.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory_type < 10 : 
            return 'LOW'
        return 'OK'
    
    @admin.action(description='Clear inventorty')
    def clear_inventory(self, request, queryset):
        updated_count=queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.ERROR
        )

    class Media:
        css = {
            'all':['store/styles.css']
        }

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 15
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id':str(customer.id)
            }))
        
        return format_html('<a href="{}">{}</a>', url, customer.orders.count())

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields= ['title']
    list_display = ['title', 'products_count']
    list_per_page = 15
    ordering = ['title']
    
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        # reverse('admin:app_model_page')
        url=(
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )


class OrderItemInline(admin.TabularInline):
    autocomplete_fifelds = ['product']
    model = models.OrderItem
    min_num = 1
    max_num = 10
    extra = 1

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    autocomplete_fields = ['customer']
    list_display = ['id', 'placed_at', 'customer']