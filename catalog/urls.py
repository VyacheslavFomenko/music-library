from django.urls import path

from catalog.views import (
    index,
    SongListView,
    SongCreateView,
    SongUpdateView,
    SongDeleteView,
    GenreListView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView, SongDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("songs/", SongListView.as_view(), name="song-list"),
    path("songs/<int:pk>/", SongDetailView.as_view(), name="song-detail"),
    path("song/create", SongCreateView.as_view(), name="song-create"),
    path("song/<int:pk>/update", SongUpdateView.as_view(), name="song-update"),
    path("song/<int:pk>/delete", SongDeleteView.as_view(), name="song-delete"),
    path("genre/", GenreListView.as_view(), name="genre-list"),
    path("genre/create", GenreCreateView.as_view(), name="genre-create"),
    path("genre/<int:pk>/update", GenreUpdateView.as_view(), name="genre-update"),
    path("genre/<int:pk>/delete", GenreDeleteView.as_view(), name="genre-delete"),
]

app_name = "catalog"
