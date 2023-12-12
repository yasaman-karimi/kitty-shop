from django.contrib import admin
from django.http import HttpRequest
from django.utils.html import format_html

from apps.product.models import Category, Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ("comment", "rate", "user")

    def has_add_permission(self, request: HttpRequest, obj):
        return False


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "image",
        "description",
        "price",
        "rating",
    )
    list_filter = (("name"),)
    fields = ("name", "price", "category", "image", "is_deleted", "image_tag")
    list_per_page = 40
    save_on_top = True
    inlines = [CommentInline]

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" width="auto" height="200px" />'.format(obj.image.url)
        )

    image_tag.short_description = "Product Image Preview"
    readonly_fields = ["image_tag"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "comment", "product")
    readonly_fields = ("user", "rate", "product")

    def has_add_permission(self, request: HttpRequest):
        return False


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
