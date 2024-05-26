from django.contrib.auth.models import AbstractUser
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Performer(AbstractUser):
    nickname = models.CharField(max_length=63, null=True, blank=True)

    class Meta:
        verbose_name = "performer"
        verbose_name_plural = "performers"

    def __str__(self):
        return f"{self.nickname} {self.first_name} {self.last_name}"


class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        ordering = ["tittle"]

    def __str__(self):
        return f"{self.title} {self.duration} {self.genre}"