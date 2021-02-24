from django.urls import path
from . import views as calendars_views

app_name = "calendars"

urlpatterns = [
    path("month", calendars_views.CalendarMonthView.as_view(), name="calendar_month"),
    path("week", calendars_views.CalendarWeekView.as_view(), name="calendar_week"),
    path("day", calendars_views.CalendarDayView.as_view(), name="calendar_day"),
    path("event/month/new/", calendars_views.create_month_event.as_view(), name="month_event_new"),
    path("event/week/new/", calendars_views.create_week_event.as_view(), name="week_event_new"),
    path("event/day/new/", calendars_views.create_day_event.as_view(), name="day_event_new"),
    path(
        "event/month/edit/<int:pk>/", calendars_views.MonthEventEdit.as_view(), name="event_month_edit"
    ),
    path(
        "event/week/edit/<int:pk>/", calendars_views.WeekEventEdit.as_view(), name="event_week_edit"
    ),
    path(
        "event/day/edit/<int:pk>/", calendars_views.DayEventEdit.as_view(), name="event_day_edit"
    ),
    path(
        "event/month/<int:event_id>/details/",
        calendars_views.event_month_details,
        name="event-month-detail",
    ),
    path(
        "event/week/<int:event_id>/details/",
        calendars_views.event_week_details,
        name="event-week-detail",
    ),
    path(
        "event/day/<int:event_id>/details/",
        calendars_views.event_day_details,
        name="event-day-detail",
    ),
    path(
        "event/month/<int:pk>/remove/",
        calendars_views.MonthEventDeleteView.as_view(),
        name="delete_month_event",
    ),
    path(
        "event/week/<int:pk>/remove/",
        calendars_views.WeekEventDeleteView.as_view(),
        name="delete_week_event",
    ),
    path(
        "event/day/<int:pk>/remove/",
        calendars_views.DayEventDeleteView.as_view(),
        name="delete_day_event",
    ),
]
