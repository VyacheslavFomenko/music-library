from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import SearchForm
from catalog.models import Song, Performer, Genre


# Create your views here.


@login_required
def index(request):
    """View function for the home page of the site."""
    num_songs = Song.objects.count()
    num_performers = Performer.objects.count()
    num_genres = Genre.objects.count()
    print(num_genres)
    print(num_songs)

    num_visits = request.session.get("num_visits", 0)
    num_visits += 1
    request.session["num_visits"] = num_visits

    context = {
        "num_songs": num_songs,
        "num_performers": num_performers,
        "num_genres": num_genres,
        "num_visits": num_visits + 1,
    }

    return render(request, "catalog/index.html", context=context)


class SongListView(generic.ListView):
    model = Song
    context_object_name = "song_list"
    template_name = "catalog/song_list.html"
    queryset = Song.objects.select_related("genre")
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(SongListView, self).get_context_data(**kwargs)
        param = self.request.GET.get("param", "")
        context["search_form"] = SearchForm(initial={"param": param})
        return context

    def get_queryset(self):
        queryset = Song.objects.select_related("genre")
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["param"])
        return queryset


class SongCreateView(generic.CreateView):
    model = Song
    fields = "__all__"
    success_url = reverse_lazy("catalog:song-list")


class SongUpdateView(generic.UpdateView):
    model = Song
    fields = "__all__"
    success_url = reverse_lazy("catalog:song-list")


class SongDeleteView(generic.DeleteView):
    model = Song
    fields = "__all__"
    success_url = reverse_lazy("catalog:song-list")


class SongDetailView(generic.DetailView):
    model = Song


class GenreListView(generic.ListView):
    model = Genre
    context_object_list = "genre_list"
    template_name = "catalog/genre_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)
        param = self.request.GET.get("param", "")
        context["search_form"] = SearchForm(initial={"param": param})
        return context

    def get_queryset(self):
        queryset = Genre.objects.all()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["param"])
        return queryset


class GenreCreateView(generic.CreateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class GenreUpdateView(generic.UpdateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class GenreDeleteView(generic.DeleteView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class PerformerListView(generic.ListView):
    model = Performer
    context_object_list = "performer_list"
    template_name = "catalog/performer_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PerformerListView, self).get_context_data(**kwargs)
        param = self.request.GET.get("param", "")
        context["search_form"] = SearchForm(initial={"param": param})
        return context

    def get_queryset(self):
        queryset = Performer.objects.all()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(last_name__icontains=form.cleaned_data["param"])
        return queryset


class PerformerDetailView(generic.DetailView):
    model = Performer


class PerformerCreateView(generic.CreateView):
    model = Performer
    fields = "__all__"
    success_url = reverse_lazy("catalog:performer-list")


class PerformerUpdateView(generic.UpdateView):
    model = Performer
    fields = "__all__"
    success_url = reverse_lazy("catalog:performer-list")


class PerformerDeleteView(generic.UpdateView):
    model = Performer
    fields = "__all__"
    success_url = reverse_lazy("catalog:performer-list")
