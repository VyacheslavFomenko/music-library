from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Performer, Genre, Song

SONG_URL = reverse("catalog:song-list")


class PublicSongFormatTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(SONG_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateCarFormatTest(TestCase):
    def setUp(self) -> None:
        self.performer = Performer.objects.create(
            first_name="Tom", last_name="Jey", nickname="TJ"
        )
        self.genre = Genre.objects.create(name="Clasic")
        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.first_song = Song.objects.create(
            title="Sonne",
            duration=3.11,
            genre=self.genre,
        )
        self.second_song = Song.objects.create(
            title="Song2",
            duration=4.11,
            genre=self.genre,
        )

        self.client.force_login(self.user)
        self.first_song.listener.add(self.user)
        self.first_song.performer.add(self.performer)
        self.second_song.listener.add(self.user)
        self.second_song.performer.add(self.performer)

    def test_song(self):
        response = self.client.get(SONG_URL)
        self.assertEqual(response.status_code, 200)
        songs = Song.objects.all()
        # print(f"Context {response.context}")
        self.assertEqual(list(response.context["song_list"]), list(songs))

        self.assertTemplateUsed(response, "catalog/song_list.html")

    def test_search_song_by_model(self):
        response = self.client.get(SONG_URL, data={"param": "Sonne"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Sonne")
        self.assertNotContains(response, "Song2")

    def test_search_car_model_not_found(self):
        response = self.client.get(SONG_URL, data={"param": "GG"})
        self.assertEqual(response.status_code, 200)

    def test_searching_car_find_all_if_name_empty(self):
        response = self.client.get(SONG_URL, {"username": ""})
        self.assertContains(response, "Sonne")
        self.assertContains(response, "Song2")


class SongChangeTest(TestCase):
    def setUp(self):
        self.performer = Performer.objects.create(
            first_name="Tom", last_name="Jey", nickname="TJ"
        )
        self.genre = Genre.objects.create(name="Clasic")
        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.first_song = Song.objects.create(
            title="Sonne",
            duration=3.11,
            genre=self.genre,
        )

        self.client.force_login(self.user)
        self.first_song.listener.add(self.user)
        self.first_song.performer.add(self.performer)

    def test_song_update_redirects_to_success_url(self):
        response = self.client.post(
            reverse("catalog:song-update", kwargs={"pk": self.first_song.pk}),
            data={
                "title": "Sonne",
                "duration": 3.11,
                "genre": self.genre.id,
                "performer": self.performer.id,
                "listener": self.user.id,
            },
        )
        self.assertRedirects(response, SONG_URL)

    def test_song_successful_deletion_redirects_to_success_url(self):
        response = self.client.post(
            reverse("catalog:song-delete", kwargs={"pk": self.first_song.pk})
        )
        self.assertRedirects(response, SONG_URL)
