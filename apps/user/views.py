from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from apps.product.models import Product
from apps.user.forms import MyRegisterForm
from apps.cart.models import Cart


class MyLoginView(LoginView):
    template_name = "user/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        session_cart = self.request.session.get("cart", {})

        if session_cart:
            user_cart = Cart.objects.get(user=self.request.user, active=True)

            for product_id, quantity in session_cart.items():
                product = get_object_or_404(Product, pk=product_id)
                user_cart.add_to_cart(product.id, quantity)

            self.request.session["cart"] = {}

        return response


class MyLogoutView(LogoutView):
    template_name = "home/index.html"


class RegisterFormView(CreateView):
    success_url = "/"
    template_name = "user/register.html"
    form_class = MyRegisterForm


@login_required
def profile(request):
    products = Product.objects.filter(designer=request.user)
    return render(
        request, "user/user.html", {"user": request.user, "products": products}
    )
