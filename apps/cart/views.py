from django.shortcuts import get_object_or_404, redirect
from django.views import View


from apps.cart.models import Cart
from apps.product.models import Product


class CartView(View):
    def add(self, request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, pk=product_id)

        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.add_to_cart(product.id)
        else:
            cart = request.session.get("cart", {})
            cart[product_id] = cart.get(product_id, 0) + 1
            request.session["cart"] = cart

        return redirect("cart")

    def delete(self, request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, pk=product_id)

        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(product.id)
        else:
            cart = request.session.get("cart", {})
            if product_id in cart:
                if cart[product_id] > 1:
                    cart[product_id] -= 1
                else:
                    del cart[product_id]
            request.session["cart"] = cart

        return redirect("cart")
