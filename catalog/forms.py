from django import forms

from catalog.models import Performer, Song, Genre


class SongForm(forms.ModelForm):
    performers = forms.ModelMultipleChoiceField(
        queryset=Performer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Song
        fields = "__all__"


class PerformerForm(forms.ModelForm):
    class Meta:
        model = Performer
        fields = "__all__"


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"


class SearchForm(forms.Form):
    param = forms.CharField(
        label="",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search"})
    )
