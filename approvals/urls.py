from django.urls import path
from . import views

app_name = "approvals"

urlpatterns = [
    path("main/", views.main, name="main"),
]
