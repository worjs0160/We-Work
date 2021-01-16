from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.utils import timezone, dateformat
from datetime import datetime
from . import models


class AttendanceHomeView(ListView):
    template_name = "attendance/main.html"
    model = models.Attendance
    context_object_name = "attendance"
    today = dateformat.format(timezone.now(), "Y-m-d")  # 현재 시간 기록
    print(today)

    def get_queryset(self):
        try:
            attendance = self.model.objects.filter(user=self.request.user).filter(
                date=self.today
            )
            attendance = attendance[0]

        except:
            attendance = False

        return attendance


def WriteStartTime(request):
    now = timezone.now()
    date = dateformat.format(now, "Y-m-d")
    work_time = dateformat.format(now, "Y-m-d H:i:s")

    # models.Attendance.objects.create(user=request.user)

    attendance = models.Attendance(user=request.user)
    attendance.save()

    return redirect(reverse("attendance:attendance_home"))


def WriteFinishTime(request):
    now = timezone.now()
    today = dateformat.format(now, "Y-m-d")
    finish_time = dateformat.format(now, "Y-m-d H:i:s")
    print(finish_time)
    try:
        attendance = models.Attendance.objects.filter(user=request.user).filter(
            date=today
        )
        attendance = attendance[0]
        attendance.time_finish_work = finish_time
        attendance.save()

    except:
        print("Error")
        return redirect(reverse("attendance:attendance_home"))

    return redirect(reverse("attendance:attendance_home"))