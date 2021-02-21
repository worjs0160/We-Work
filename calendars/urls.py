from django.urls import path
from . import views as calendars_views

app_name = "calendars"

urlpatterns = [
    path("month", calendars_views.CalendarView.as_view(), name="calendar_month"),
    path("week", calendars_views.CalendarWeekView.as_view(), name="calendar_week"),
    path("day", calendars_views.CalendarDayView.as_view(), name="calendar_day"),
    path("event/month/new/", calendars_views.create_month_event.as_view(), name="month_event_new"),
    path("event/week/new/", calendars_views.create_week_event.as_view(), name="week_event_new"),
    path("event/day/new/", calendars_views.create_day_event.as_view(), name="day_event_new"),
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
