from django.contrib import admin

from mainapp.models import ProductCategory, Product
from authapp.models import User

# admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(User)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    readonly_fields = ('short_description',)
    ordering = ('name',)
    search_fields = ('name',)