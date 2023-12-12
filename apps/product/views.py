from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View

from apps.product.forms import ProductForm, CommentForm
from apps.product.models import Product, Comment, Category


class ProductsListView(ListView):
    model = Product
    template_name = "product/all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context


class OneProductView(DetailView):
    model = Product
    template_name = "product/single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.filter(is_confirmed=True)

        return context


class MyProductList(ListView, LoginRequiredMixin):
    template_name = "product/my/all.html"

    def get_queryset(self):
        return Product.objects.filter(designer=self.request.user)


class MyProductCreate(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = "product/my/create.html"
    success_url = "/myproducts"

    def form_valid(self, form):
        form.instance.designer = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class MyProductUpdate(UpdateView, LoginRequiredMixin):
    form_class = ProductForm
    template_name = "product/my/edit.html"
    success_url = "/myproducts"

    def get_queryset(self):
        return Product.objects.filter(designer=self.request.user)


class MyProductDelete(View):
    http_method_names = ("post",)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk, designer=request.user)
        product.is_deleted = True
        product.save()
        return redirect("list_myproduct")


class CreateComment(CreateView):
    model = Comment
