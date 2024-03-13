from django.contrib import admin

from catalog.models import Product, Category, ContactDetails


# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category"]
    search_fields = ["name", "description"]
    list_filter = ["category", ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", ]


@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", ]
