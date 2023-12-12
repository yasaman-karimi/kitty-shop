from django.shortcuts import render

from apps.product.models import Product, Category


def home(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(
        request,
        "home/index.html",
        context={"products": product, "categories": category},
    )
