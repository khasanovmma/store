from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from product.models import Brand, Category, Product, ProductImage, ProductPrice


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("product", "photo", "photo_preview", "order")
    readonly_fields = ("photo_preview",)
    raw_id_fields = ("product",)
    list_select_related = ("product",)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "quantity",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)
    inlines = (ProductImageInline,)


@admin.register(ProductPrice)
class ProductPriceModelAdmin(admin.ModelAdmin):
    list_display = ("product", "price", "created_at", "updated_at")


@admin.register(Category)
class CategoryModelAdmin(MPTTModelAdmin):
    list_display = ("name", "is_active", "created_at", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_name",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "short_name")
