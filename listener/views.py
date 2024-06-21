from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from listener.models import Listener


# Create your views here.

class ListenerDetailView(generic.DetailView):
    model = Listener


class ListenerDeleteView(generic.DeleteView):
    model = Listener
    success_url = reverse_lazy("catalog:index")


class ListenerUpdateView(generic.CreateView):
    model = Listener
    fields = "__all__"
    success_url = reverse_lazy("catalog:index")
