from datetime import datetime, date
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView,
)
from django.contrib.auth import get_user_model
from .models import Calendar, File
from .utils import Calendar_u
from .forms import EventForm

UserModel = get_user_model()


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


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


class CalendarView(generic.ListView):

    model = Calendar
    template_name = "calendar_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar_u(d.year, d.month)
        html_cal = cal.formatmonth(self.request.user, withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


class create_event(BSModalCreateView):
    template_name = "calendars/event.html"
    form_class = EventForm
    success_message = "Sucess: Event was created"
    success_url = reverse_lazy("calendars:calendar")
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            calendar= form.save()
            calendar.user = request.user
            calendar.save()
            
            file = request.FILES.get("attached_file")

            if file:
                File.objects.create(file=file, calendar=calendar)
            else:
                File.objects.create(calendar=calendar)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    


class EventEdit(BSModalUpdateView):
    model = Calendar
    template_name = "calendars/event_edit.html"
    form_class = EventForm
    success_message = "Success: Event was updated."
    success_url = reverse_lazy("calendars:calendar")


def event_details(request, event_id):
    event = Calendar.objects.get(id=event_id)
    context = {"event": event}
    return render(request, "calendars/event-details.html", context)


class EventDeleteView(BSModalDeleteView):
    model = Calendar
    template_name = "calendars/event_delete.html"
    success_message = "Success: Event was deleted."
    success_url = reverse_lazy("calendars:calendar")
