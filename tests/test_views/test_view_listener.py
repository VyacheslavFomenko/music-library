from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from listener.forms import ListenerCreationForm

# LISTENER_URL = reverse("listener:listener-detail")

LISTENER_DATA = {"username": "test", "password1": "Test1234q", "password2": "Test1234q"}


class PrivateListenerFormatTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        get_user_model().objects.create_user(
            username="somebody",
            password="test123",
        )

        self.client.force_login(self.user)
        for i in range(1, 5):
            get_user_model().objects.create_user(
                username=f"test_0{i}",
                password="test123",
            )

    def test_create_listener(self):
        form_data = {
            "username": "new_user",
            "password1": "user1234test",
            "password2": "user1234test",
            "first_name": "Test first",
            "last_name": "Test last",
        }
        self.client.post(reverse("listener:listener-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])
        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])


class DriverChangeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="Test1234q",
        )

        self.client.force_login(self.user)

    def test_successful_driver_creation(self):
        response = self.client.post(
            reverse("listener:listener-create"), data=LISTENER_DATA
        )
        listener = get_user_model().objects.get(username="test")
        self.assertEqual(response.status_code, 302)

        self.assertTrue(get_user_model().objects.filter(username="test").exists())
        self.assertRedirects(
            response, reverse("listener:listener-detail", kwargs={"pk": listener.pk})
        )

    def test_unsuccessful_listener_creation(self):
        data = {"username": "test"}
        response = self.client.post(reverse("listener:listener-create"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(get_user_model().objects.filter(username="test").exists())

    def test_listener_creation_form_displayed_on_page(self):
        response = self.client.get(reverse("listener:listener-create"))
        self.assertIsInstance(response.context["form"], ListenerCreationForm)

    def test_listener_successful_deletion_redirects_to_success_url(self):
        self.client.post(
            reverse("listener:listener-delete", kwargs={"pk": self.user.pk})
        )
        self.assertFalse(get_user_model().objects.filter(pk=self.user.pk).exists())
