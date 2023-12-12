from django.urls import path

from apps.user.views import MyLoginView, MyLogoutView, RegisterFormView, profile

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", RegisterFormView.as_view(), name="register"),
    path("myprofile/", profile, name="myprofile"),
]
