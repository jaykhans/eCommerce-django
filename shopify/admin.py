from django.contrib import admin
from .models import * 
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderedProduct)
class OrderedItemAdmin(admin.ModelAdmin):
    pass

