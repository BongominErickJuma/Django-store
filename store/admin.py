from django.contrib import admin
from . import models
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_per_page = 10
    list_select_related = ["collection"]
    list_filter = ["collection", "last_updated"]


    def collection_title(self, product):
        return product.collection.title

    def inventory_status(self, product):
        if(product.inventory < 100):
            return "LOW"
        return "OK"
    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user__first_name", "user__last_name", "membership", "orders"]
    list_editable = ["membership"]
    list_per_page = 5
    list_select_related = ['user']
    ordering = ["user__first_name", "user__last_name"]
    search_fields = ["first_name__istartswith", "last_name__istartswith"]

    def orders(self, customer):
        url = (reverse('admin:store_order_changelist') + "?" + urlencode({'customer__id': str(customer.id)}))
        return format_html('<a href="{}">{}</a>',url, customer.orders)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders = Count("order")
        )

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "payment_status", "customer"]
    ordering = ["-id"]
    list_per_page = 10
    list_editable=["payment_status"]
    list_select_related = ["customer"]

    def customer(self, order):
        return f"{order.customer.first_name} {order.customer.last_name}"

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"]

    def products_count(self, collection):
        url = (reverse('admin:store_product_changelist') + "?" + urlencode({'collection__id': str(collection.id)}))
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count("product")
        )