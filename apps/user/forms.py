from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.user.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(min_length=8, max_length=128, widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)


class UserForm(forms.ModelForm):
    password2 = forms.CharField(
        min_length=8, max_length=128, widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "about",
            "avatar",
        )


class MyRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("avatar", "about")
