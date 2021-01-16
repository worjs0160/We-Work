from django.urls import path
from . import views

app_name = "messengers"

urlpatterns = [
    path("", views.UserView.as_view(), name="messenger"),
    path("go/<int:my_pk>/<int:your_pk>/", views.go_msg_room, name="go"),
    path("<int:pk>/", views.MessengerRoomView.as_view(), name="detail"),
]
