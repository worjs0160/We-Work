from django.urls import path
from . import views

app_name = "approvals"

urlpatterns = [
    path("main/", views.main, name="main"),
    path("main/doc_format/<str:doc>", views.doc_format),
    path("main/new_doc", views.new_doc),
    path("create/", views.createDocView, name="create"),
    path("main/my_doc_list/", views.ListMyDocView, name="my_doc_list"),
    path("main/view_doc_list/", views.ListViewDocView, name="view_doc_list"),
    path(
        "main/approval_doc_list/", views.ListApprovalDocView, name="approval_doc_list"
    ),
    path(
        "detail/<int:doc_pk>-<str:doc_type>-<str:doc_path>/",
        views.DetailView,
        name="detail",
    ),
]
