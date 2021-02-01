from django.urls import path
from . import views

app_name = "papers"

urlpatterns = [
    path("paper-main/", views.paper_main, name="paper-main"),
]
