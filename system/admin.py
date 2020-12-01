from django.contrib import admin
from system.models import Category, Subcategory, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'subcategory', 'price', 'size', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price', 'size']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
