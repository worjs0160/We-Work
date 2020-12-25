from django.urls import path
from . import views as boards_views

app_name = "boards"

urlpatterns = [
    path("board_list/", boards_views.readBoardList, name="board_read"),
    path("board_list/delete/<int:pk>/", boards_views.deleteBoard, name="board_delete"),
    path("<int:pk>/", boards_views.readBoardDetail, name="board_detail"),
]
