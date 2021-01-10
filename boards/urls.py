from django.urls import path
from . import views as boards_views

app_name = "boards"

urlpatterns = [
    path("board_list/", boards_views.readBoardList, name="board_list"),
    path("create/", boards_views.CreateBoardView.as_view(), name="create"),
    path("<int:pk>/", boards_views.BoardDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", boards_views.UpdateBoardView.as_view(), name="update"),
    path("<int:pk>/delete/", boards_views.deleteBoard, name="delete"),
    path("<int:pk>/comment_create/", boards_views.createComment, name="comment_create"),
    path("<int:pk>/comment_delete/", boards_views.deleteComment, name="comment_delete"),
]
