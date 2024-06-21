from django.contrib.auth.models import AbstractUser
from django.db import models

from listener.models import Listener


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Performer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=63, null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.nickname} {self.first_name} {self.last_name}"


class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="genre")
    performer = models.ManyToManyField(Performer, related_name="performer")
    listener = models.ManyToManyField(Listener, related_name="songs")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} {self.duration} {self.genre}."
