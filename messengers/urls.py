from django.urls import path
from . import views

app_name = "messengers"

urlpatterns = [
    path("", views.go_lobby, name="go_lobby"),
    path("<str:room_name>/", views.room, name="room"),
    path("<str:pk1>_<str:pk2>", views.go_room, name="go_room"),
]
