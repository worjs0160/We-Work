from django.urls import path
from . import views

app_name = "attendance"

urlpatterns = [
    path(
        "attendance_home/",
        views.AttendanceHomeView.as_view(),
        name="attendance_home",
    ),
    path("attendance_home/start_work", views.WriteStartTime, name="start_work"),
    path("attendance_home/finish_work", views.WriteFinishTime, name="finish_work"),
]
