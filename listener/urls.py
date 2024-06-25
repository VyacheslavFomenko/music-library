from django.urls import path

from listener.views import ListenerDetailView, ListenerDeleteView, ListenerCreatView, ListenerUpdateView

urlpatterns = [
    path("listener/<int:pk>/", ListenerDetailView.as_view(), name="listener-detail"),
    path("listener/<int:pk>/delete", ListenerDeleteView.as_view(), name="listener-delete"),
    path(
        "listener/<int:pk>/update/",
        ListenerUpdateView.as_view(),
        name="listener-update",
    ),
    path("listener/create/", ListenerCreatView.as_view(), name="listener-create"),
]

app_name = "listener"
