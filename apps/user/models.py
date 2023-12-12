from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/", blank=True)
    about = models.TextField(blank=True)

    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return f"Ms/Mr {self.last_name}"
        else:
            return "Kitty"
