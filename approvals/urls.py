from django.urls import path
from . import views

app_name = "approvals"

urlpatterns = [
    path("main/", views.main, name="main"),
    path("main/doc_format/<str:doc>", views.doc_format),
    path("main/new_doc", views.new_doc),
    path("create/", views.createDocView, name="create"),
    path("list/", views.ListMyDocView, name="list"),
    path(
        "detail/<int:doc_pk><str:doc_type><str:doc_path>/",
        views.DetailView,
        name="detail",
    ),
]
