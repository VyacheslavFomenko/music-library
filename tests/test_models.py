from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import Song, Performer, Genre


class TestModels(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(
            name="Rock",
        )

        self.listener = get_user_model().objects.create(
            username="listener",
            first_name="Nick",
            last_name="Gordon",
            password="test_password",
        )

        self.performer = Performer.objects.create(
            first_name="Mick", last_name="Gordon", nickname="Mick"
        )

    def test_genre_str(self):
        self.assertEqual(str(self.genre), f"{self.genre.name}")

    def test_listener_str(self):
        self.assertEqual(
            str(self.listener),
            f"{self.listener.username}, {self.listener.first_name}, {self.listener.last_name}.",
        )

    def test_performer_str(self):
        self.assertEqual(
            str(self.performer),
            f"{self.performer.nickname} {self.performer.first_name} {self.performer.last_name}",
        )

    def test_song_str(self):
        song = Song.objects.create(
            title="Song 2",
            duration=3.11,
            genre=self.genre,
        )

        self.assertEqual(
            str(song),
            f"Song title: {song.title}, Duration: {song.duration} min/sec, "
            f"Genre: {song.genre}.",
        )
