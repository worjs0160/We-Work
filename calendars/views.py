from datetime import datetime, date, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
from django.utils import timezone, dateformat
import calendar
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView,
)
from django.contrib.auth import get_user_model
from .models import Calendar, File
from .utils import Calendar_u, Calendar_Week, Calendar_Day
from .forms import EventForm

UserModel = get_user_model()

# 월간으로 보기 - start

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

# 월간으로 보기 - end

# 주간으로 보기 - start

def get_week_date(req_day):
    if req_day:
        year, month, day = (int(x) for x in req_day.split("-"))
        return date(year, month, day)
    return datetime.today()


def prev_week(d):
    first = d
    prev_week = first - timedelta(days=7)
    week = "week=" + str(prev_week.year) + "-" + \
        str(prev_week.month) + "-" + str(prev_week.day)
    return week


def next_week(d):
    first = d
    next_week = first + timedelta(days=7)
    week = "week=" + str(next_week.year) + "-" + \
        str(next_week.month) + "-" + str(next_week.day)
    return week

# 주간으로 보기 - end

# 일간으로 보기 - start

def get_day_date(req_day):
    if req_day:
        year, month, day = (int(x) for x in req_day.split("-"))
        return date(year, month, day)
    return datetime.today()


def prev_day(d):
    first = d
    prev_day = first - timedelta(days=1)
    day = "day=" + str(prev_day.year) + "-" + \
        str(prev_day.month) + "-" + str(prev_day.day)
    return day


def next_day(d):
    first = d
    next_day = first + timedelta(days=1)
    day = "day=" + str(next_day.year) + "-" + \
        str(next_day.month) + "-" + str(next_day.day)
    return day

# 일간으로 보기 - end

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


class CalendarView(generic.ListView):

    model = Calendar
    template_name = "calendars/calendar_month_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar_u(d.year, d.month)
        html_cal = cal.formatmonth(self.request.user, withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


class create_month_event(BSModalCreateView):
    template_name = "calendars/event.html"
    form_class = EventForm
    success_message = "Sucess: Event was created"
    success_url = reverse_lazy("calendars:calendar_month")
    
    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        if self.request.is_ajax():
            calendar = form.save()
            calendar.user = self.request.user
            calendar.save()
            file = self.request.FILES.get("file")
            if file:
                File.objects.create(file=file, calendar=calendar)
            else:
                File.objects.create(calendar=calendar)

        return HttpResponseRedirect(reverse_lazy("calendars:calendar_month"))
    

class EventEdit(BSModalUpdateView):
    model = Calendar
    template_name = "calendars/event_edit.html"
    form_class = EventForm
    success_message = "Success: Event was updated."
    success_url = reverse_lazy("calendars:calendar_month")


def event_details(request, event_id):
    event = Calendar.objects.get(id=event_id)
    context = {"event": event}
    return render(request, "calendars/event-details.html", context)


class EventDeleteView(BSModalDeleteView):
    model = Calendar
    template_name = "calendars/event_delete.html"
    success_message = "Success: Event was deleted."
    success_url = reverse_lazy("calendars:calendar_month")


class CalendarWeekView(generic.ListView):

    model = Calendar
    template_name = "calendars/calendar_week_list.html"
    # today = dateformat.format(timezone.now(), "Y-m-d")  # 현재 시간 기록

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #  현재 날짜 받아오기
        d = get_week_date(self.request.GET.get("week", None))

        # 달력을 출력할 날짜 포맷팅 기능 세팅
        cal = Calendar_Week(d.year, d.month, d.day)
        html_cal = cal.formatmonth(self.request.user, withyear=True)
        # print(d, "ddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaa")
        context["calendar"] = mark_safe(html_cal)
        context["prev_week"] = prev_week(d)
        context["next_week"] = next_week(d)

        return context

class create_week_event(BSModalCreateView):
    template_name = "calendars/event.html"
    form_class = EventForm
    success_message = "Sucess: Event was created"
    success_url = reverse_lazy("calendars:calendar_week")
    
    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        if self.request.is_ajax():
            calendar = form.save()
            calendar.user = self.request.user
            calendar.save()
            file = self.request.FILES.get("file")
            if file:
                File.objects.create(file=file, calendar=calendar)
            else:
                File.objects.create(calendar=calendar)

        return HttpResponseRedirect(reverse_lazy("calendars:calendar_week"))


class CalendarDayView(generic.ListView):

    model = Calendar
    template_name = "calendars/calendar_day_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_day_date(self.request.GET.get("day", None))

        cal = Calendar_Day(d.year, d.month, d.day)
        html_cal = cal.formatmonth(self.request.user, withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_day"] = prev_day(d)
        context["next_day"] = next_day(d)

        return context

class create_day_event(BSModalCreateView):
    template_name = "calendars/event.html"
    form_class = EventForm
    success_message = "Sucess: Event was created"
    success_url = reverse_lazy("calendars:calendar_day")
    
    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        if self.request.is_ajax():
            calendar = form.save()
            calendar.user = self.request.user
            calendar.save()
            file = self.request.FILES.get("file")
            if file:
                File.objects.create(file=file, calendar=calendar)
            else:
                File.objects.create(calendar=calendar)

        return HttpResponseRedirect(reverse_lazy("calendars:calendar_day"))