from django.urls import path
from . import views as boards_views

app_name = "boards"

urlpatterns = [
    path("board_list/", boards_views.board_list, name="board_list"),
    path("test", boards_views.test, name="test"),
]
