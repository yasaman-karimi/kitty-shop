from django import forms

from apps.product.models import Product, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "category",
            "price",
            "description",
            "image",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "user",
            "rate",
            "comment",
            "is_verified_buyer",
            "is_confirmed",
        )
