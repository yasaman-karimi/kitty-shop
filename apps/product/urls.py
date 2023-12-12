from django.urls import path

from .views import (
    ProductsListView,
    OneProductView,
    MyProductList,
    MyProductCreate,
    MyProductUpdate,
    MyProductDelete,
)

urlpatterns = [
    path("products/", ProductsListView.as_view(), name="list_product"),
    path("products/<int:pk>/", OneProductView.as_view(), name="detail_product"),
    path("myproducts", MyProductList.as_view(), name="list_myproduct"),
    path("myproducts/add", MyProductCreate.as_view(), name="add_myproduct"),
    path("myproducts/<int:pk>", MyProductUpdate.as_view(), name="update_myproduct"),
    path(
        "myproducts/delete/<int:pk>", MyProductDelete.as_view(), name="delete_myproduct"
    ),
]
