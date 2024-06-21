from django.urls import path

from listener.views import ListenerDetailView, ListenerDeleteView

urlpatterns = [
    path("listener/<int:pk>/", ListenerDetailView.as_view(), name="listener-detail"),
    path("performer/<int:pk>/delete", ListenerDeleteView.as_view(), name="listener-delete"),
]

app_name = "listener"
