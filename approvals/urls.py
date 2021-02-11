from django.urls import path
from . import views

app_name = "approvals"

urlpatterns = [
    path("main/", views.main, name="main"),
    path("main/doc_format/<str:doc>", views.doc_format),
    path("create/", views.createDocView, name="create"),
    path("list/", views.ListMyDocView, name="list"),
    path("detail/<int:pk>", views.DetailView, name="detail"),
]
