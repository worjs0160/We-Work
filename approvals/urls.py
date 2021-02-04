from django.urls import path
from . import views

app_name = "approvals"

urlpatterns = [
    path("main/", views.main, name="main"),
    path("main/doc_format/<str:doc>", views.doc_format),
]
