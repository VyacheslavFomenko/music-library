from django.contrib import admin

from catalog.models import Song, Genre, Performer

# Register your models here.

admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Performer)
