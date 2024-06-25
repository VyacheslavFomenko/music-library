from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from listener.forms import ListenerCreationForm
from listener.models import Listener


# Create your views here.

class ListenerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Listener


class ListenerCreatView(LoginRequiredMixin, generic.CreateView):
    model = Listener
    form_class = ListenerCreationForm


class ListenerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Listener
    success_url = reverse_lazy("catalog:index")


class ListenerUpdateView(LoginRequiredMixin, generic.CreateView):
    model = Listener
    fields = "__all__"
    success_url = reverse_lazy("catalog:index")
