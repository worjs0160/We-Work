from django.urls import path
from . import views as boards_views

app_name = "boards"

urlpatterns = [
    path("board_list/", boards_views.readBoardList, name="board_list"),
    path("board_create/", boards_views.CreateBoardView.as_view(), name="board_create"),
    path(
        "board_update/<int:pk>/",
        boards_views.UpdateBoardView.as_view(),
        name="board_update",
    ),
    path("delete/<int:pk>/", boards_views.deleteBoard, name="board_delete"),
    path("<int:pk>/", boards_views.BoardDetailView.as_view(), name="board_detail"),
]
