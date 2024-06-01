from msilib.schema import ListView

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from catalog.models import Song, Performer, Genre


# Create your views here.

@login_required
def index(request):
    """View function for the home page of the site."""
    num_songs = Song.objects.all().count()
    num_performers = Performer.objects.all().count()
    num_genres = Genre.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        "num songs": num_songs,
        "num performers": num_performers,
        "num genres": num_genres,
        "num visits": num_visits + 1,
    }

    return render(request, "catalog/index.html", context=context)




