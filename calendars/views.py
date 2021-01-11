from datetime import datetime, date
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView,
)

from .models import Calendar
from .utils import Calendar_u
from .forms import EventForm
from django.http import Http404


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


class CalendarView(generic.ListView):

    model = Calendar
    context_object_name = "users"
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar_u(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


class create_event(BSModalCreateView):

    template_name = "calendars/event.html"
    form_class = EventForm
    success_message = "Sucess: Event was created"
    success_url = reverse_lazy("calendars:calendar")


class EventEdit(generic.UpdateView):
    model = Calendar

    fields = ["title", "schedule", "start_time", "end_time"]
    template_name = "calendars/event.html"


def event_details(request, event_id):
    event = Calendar.objects.get(id=event_id)
    context = {"event": event}
    return render(request, "calendars/event-details.html", context)


class EventDeleteView(generic.DeleteView):
    model = Calendar
    template_name = "calendars/event_delete.html"
    success_url = reverse_lazy("calendars:calendar")


def go_create_event(request, i_pk):
    user = Calendar.objects.get(i_pk=pk)
