from django.contrib import admin

import src.core.models as models


# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ("id", "name")
    list_display = ("id", "name", "added_at", "updated_at")


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "added_at", "updated_at")


class ProductImageInline(admin.TabularInline):
    extra = 1
    model = models.ProductImage


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    inlines = [ProductImageInline]
    list_display_links = ("id", "name")
    list_filter = ("added_at", "category")
    list_display = ("id", "name", "category", "price", "stock", "added_at", "updated_at")


@admin.register(models.Stock)
class StockAdmin(admin.ModelAdmin):
    list_filter = ("added_at",)
    list_display = ("id", "product", "quantity", "price", "total_sum", "added_at", "updated_at")


@admin.register(models.Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_filter = ("added_at",)
    list_display_links = ("id", "user")
    list_display = ("id", "user", "product", "added_at")


class CartItemInline(admin.TabularInline):
    extra = 0
    model = models.CartItem


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display_links = ("id", "owner")
    list_filter = ("added_at", "is_active")
    list_display = ("id", "owner", "total_price", "is_active", "added_at")


@admin.register(models.Billing)
class BillingAdmin(admin.ModelAdmin):
    list_filter = ("added_at",)
    list_display_links = ("id", "f_name")
    search_fields = ("f_name", "phone", "ex_phone")
    list_display = ("id", "f_name", "address", "phone", "ex_phone", "added_at")


class OrderItemInline(admin.TabularInline):
    extra = 0
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_filter = ("added_at",)
    list_display_links = ("id", "owner")
    list_display = ("id", "owner", "total_price", "added_at")


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
