from django.urls import path
from . import views as calendars_views

app_name = "calendars"

urlpatterns = [
    path("month", calendars_views.CalendarView.as_view(), name="calendar_month"),
    path("week", calendars_views.CalendarWeekView.as_view(), name="calendar_week"),
    path("day", calendars_views.CalendarDayView.as_view(), name="calendar_day"),
    path("event/new/", calendars_views.create_event.as_view(), name="event_new"),
    path(
        "event/edit/<int:pk>/", calendars_views.EventEdit.as_view(), name="event_edit"
    ),
    path(
        "event/<int:event_id>/details/",
        calendars_views.event_details,
        name="event-detail",
    ),
    path(
        "event/<int:pk>/remove/",
        calendars_views.EventDeleteView.as_view(),
        name="delete_event",
    ),
]
