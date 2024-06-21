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
    GenreDeleteView, SongDetailView, PerformerListView, PerformerCreateView, PerformerUpdateView, PerformerDeleteView,
    PerformerDetailView, add_song_to_favorites
)

urlpatterns = [
    path("", index, name="index"),
    path("songs/", SongListView.as_view(), name="song-list"),
    path("songs/<int:pk>/", SongDetailView.as_view(), name="song-detail"),
    path("song/create", SongCreateView.as_view(), name="song-create"),
    path("song/<int:pk>/update", SongUpdateView.as_view(), name="song-update"),
    path("song/<int:pk>/delete", SongDeleteView.as_view(), name="song-delete"),
    path("song/<int:pk>/add-to-favourite-song", add_song_to_favorites, name="add-to-favourite-song"),
    path("genre/", GenreListView.as_view(), name="genre-list"),
    path("genre/create", GenreCreateView.as_view(), name="genre-create"),
    path("genre/<int:pk>/update", GenreUpdateView.as_view(), name="genre-update"),
    path("genre/<int:pk>/delete", GenreDeleteView.as_view(), name="genre-delete"),
    path("performer/", PerformerListView.as_view(), name="performer-list"),
    path("performer/create", PerformerCreateView.as_view(), name="performer-create"),
    path("performer/<int:pk>/update", PerformerUpdateView.as_view(), name="performer-update"),
    path("performer/<int:pk>/delete", PerformerDeleteView.as_view(), name="performer-delete"),
    path("performer/<int:pk>/", PerformerDetailView.as_view(), name="performer-detail"),

]

app_name = "catalog"
