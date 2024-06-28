from django.contrib.auth.forms import UserCreationForm

from listener.models import Listener


class ListenerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Listener
        fields = ("username", "first_name", "last_name", "password1", "password2")
