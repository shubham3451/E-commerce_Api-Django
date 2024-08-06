from django.contrib import admin
from .models import *

#Register your models here.
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Brand)
class brandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_digital')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin): 
    list_display = ('id', 'url', 'alt_text', )
    search_fields = ('name', 'alt_text')

@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    list_display = ('id','price', 'sku', 'stock_qty')

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')

