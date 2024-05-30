from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Listener(AbstractUser):
    class Meta:
        ordering = ('username',)

    def __str__(self):
        return f"{self.username}, {self.first_name}, {self.last_name}."
