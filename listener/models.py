from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.
class Listener(AbstractUser):
    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}, {self.first_name}, {self.last_name}."

    def get_absolute_url(self):
        return reverse("listener:listener-detail", kwargs={"pk": self.pk})
