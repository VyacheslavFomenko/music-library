from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

from catalog.models import Performer

PERFORMER_URL = reverse("catalog:performer-list")


class PublicPerformerFormatTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(PERFORMER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivatePerformerFormatTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.client.force_login(self.user)

        self.performer1 = (
            Performer.objects.create(first_name="t1", last_name="tt", nickname="ttt"),
        )
        self.performer2 = Performer.objects.create(
            first_name="t2", last_name="tt2", nickname="ttt2"
        )

    def test_performer(self):
        response = self.client.get(PERFORMER_URL)

        self.assertEqual(response.status_code, 200)

        performer = Performer.objects.all()

        self.assertEqual(list(response.context["performer_list"]), list(performer))

        self.assertTemplateUsed(response, "catalog/performer_list.html")

    def test_search_performer_by_name(self):
        response = self.client.get(PERFORMER_URL, data={"param": "t1"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "t1")
        self.assertNotContains(response, "t2")

    def test_search_performer_name_not_found(self):
        response = self.client.get(PERFORMER_URL, data={"param": "GG"})
        self.assertEqual(response.status_code, 200)


class PerformerChangeTests(TestCase):
    def setUp(self):
        self.performer = Performer.objects.create(
            first_name="t1", last_name="tt", nickname="ttt"
        )

        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.client.force_login(self.user)

    def test_performer_update_redirects_to_success_url(self):
        response = self.client.post(
            reverse("catalog:performer-update", kwargs={"pk": self.performer.pk}),
            data={"first_name": "GG", "last_name": "Dep", "nickname": "ttt"},
        )

        self.assertRedirects(response, PERFORMER_URL)

    def test_performer_successful_deletion_redirects_to_success_url(self):
        response = self.client.post(
            reverse("catalog:performer-delete", kwargs={"pk": self.performer.pk})
        )
        self.assertRedirects(response, PERFORMER_URL)
