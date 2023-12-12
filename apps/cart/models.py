from django.db import models
from django.contrib.auth import get_user_model

from apps.product.models import Product


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, through="CartProduct")
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)

    def add_to_cart(self, product_id):
        product = Product.objects.get(pk=product_id)
        cart_product, created = CartProduct.objects.get_or_create(
            product=product, cart=self, defaults={"quantity": 0}
        )
        cart_product.quantity += 1
        cart_product.save()

    def remove_from_cart(self, product_id):
        product = Product.objects.get(pk=product_id)
        cart_product = CartProduct.objects.get(product=product, cart=self)
        if cart_product.quantity > 1:
            cart_product.quantity -= 1
            cart_product.save()
        else:
            cart_product.delete()
