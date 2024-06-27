from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.forms import SongForm, PerformerForm, GenreForm, SearchForm
from catalog.models import Performer, Genre, Song
from listener.forms import ListenerCreationForm

LISTENER_DATA = {"username": "test", "password1": "Test1234q", "password2": "Test1234q"}


class SongFormTest(TestCase):
    def test_car_form_valid_creation(self):
        performer = Performer.objects.create(
            first_name="Tom", last_name="Jey", nickname="TJ"
        )
        genre = Genre.objects.create(name="Clasic")
        user = get_user_model().objects.create_user(username="test", password="test123")

        form_data = {
            "Title": "Sonne",
            "Duration": 3.11,
            "Genre": genre.id,
            "Performer": performer.id,
            "Listener": user.id,
        }
        form = SongForm(data=form_data)
        print(form.data)
        self.assertFalse(form.is_valid())

    def test_song_form_invalid_creation(self):
        form_data = {"duration": "model_test"}
        form = SongForm(data=form_data)
        self.assertFalse(form.is_valid())


class GenreFormTest(TestCase):
    def test_genre_form_valid_creation(self):
        form_data = {"name": "djazz"}
        form = GenreForm(data=form_data)
        self.assertTrue(form.is_valid())


class PerformerFormTest(TestCase):
    def test_performer_valid_creation(self):
        form = PerformerForm(
            data={
                "first_name": "test_f_n",
                "last_name": "test_l_n",
                "nickname": "test_nick",
            }
        )
        self.assertTrue(form.is_valid())

    def test_performer_form_invalid_creation(self):
        form_data = {"first_name": "test_f_n"}
        form = PerformerForm(data=form_data)
        self.assertFalse(form.is_valid())


class ListenerFormTest(TestCase):
    def test_listener_valid_creation(self):
        form = ListenerCreationForm(data=LISTENER_DATA)
        self.assertTrue(form.is_valid())

    def test_listener_form_invalid_creation(self):
        form_data = {"first_name": "test_f_n"}
        form = PerformerForm(data=form_data)
        self.assertFalse(form.is_valid())
