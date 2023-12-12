from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.db.models import Avg


class Category(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Categories"


class ProductModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Product(models.Model):
    designer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="product/")
    is_deleted = models.BooleanField(default=False)

    objects = ProductModelManager()
    all_objects = models.Manager()

    def rating(self):
        rating = self.comments.aggregate(rate=Avg("rate"))["rate"] or 0
        return round(rating, 2)

    def show_comments(self):
        return Comment.objects.order_by("-comment")[:9]

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )
    rate = models.PositiveIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(10))
    )
    comment = models.CharField(max_length=128)
    is_verified_buyer = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
