from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls.base import reverse

from catalog.models import Genre

GENRE_URL = reverse("catalog:genre-list")


class PublicGenreFormatTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(GENRE_URL)
        self.assertNotEquals(res.status_code, 200)


class PrivateGenreFormatTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.client.force_login(self.user)

    def test_genre(self):
        Genre.objects.create(name="Rock"),
        Genre.objects.create(name="POP")

        response = self.client.get(GENRE_URL)

        self.assertEqual(response.status_code, 200)

        genre = Genre.objects.all()

        self.assertEqual(list(response.context["genre_list"]), list(genre))

        self.assertTemplateUsed(response, "catalog/genre_list.html")

    def test_search_genre_by_name(self):
        Genre.objects.create(name="KPOP")
        Genre.objects.create(name="Hip-Hop")

        response = self.client.get(GENRE_URL, data={"param": "KP"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "KPOP")
        self.assertNotContains(response, "Hip-Hop")

    def test_search_genre_name_not_found(self):
        response = self.client.get(GENRE_URL, data={"param": "GG"})
        self.assertEqual(response.status_code, 200)


class GenreChangeTests(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(
            name="POP",
        )

        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.client.force_login(self.user)

    def test_genre_update_redirects_to_success_url(self):
        response = self.client.post(
            reverse("catalog:genre-update", kwargs={"pk": self.genre.pk}),
            data={"name": "GLAM"},
        )
        self.assertRedirects(response, GENRE_URL)

    def test_genre_successful_deletion_redirects_to_success_url(self):
        response = self.client.post(
            reverse("taxi:manufacturer-delete", kwargs={"pk": self.genre.pk})
        )
        self.assertRedirects(response, GENRE_URL)
