import os, datetime
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from boards import models as board_models
from attendance import models as attendance_models

# 이번주의 월요일과 일요일 날짜구하는 함수
def get_week_date():
    cnt = datetime.date.today().weekday()
    start_week = datetime.date.today() + datetime.timedelta(-cnt)
    end_week = datetime.date.today() + datetime.timedelta(6 - cnt)
    return start_week, end_week, cnt


# 일주일간의 근태 쿼리에서 근무시간 계산하는 함수
def get_week_work(start_week, end_week, week_attendances):
    tmp = []
    time_work = []

    for date in range(start_week.day, end_week.day + 1):
        try:
            info = week_attendances.filter(date__day=date)[0]
            tmp.append(info)
            work = info.time_finish_work - info.time_start_work
            time_work.append(work.seconds / (60 * 60))
        except:
            tmp.append(0)
            time_work.append(0)

    return tmp, time_work


# 홈페이지 로딩
@login_required
def home(request):
    # 이번주 첫째(월)와 마지막 요일(금) 가져오기
    start_week, end_week, cnt = get_week_date()

    print("월요일: " + str(start_week) + " 일요일: " + str(end_week) + " cnt: " + str(cnt))

    # 일주일간의 근태 데이터 가져오기
    week_attendances = (
        attendance_models.Attendance.objects.filter(user=request.user)
        .filter(date__range=[start_week, end_week + datetime.timedelta(days=1)])
        .order_by("date")
    )

    tmp, time_work = get_week_work(start_week, end_week, week_attendances)
    print("time_work: " + str(time_work))

    boards = board_models.Board.objects.order_by("-updated")[:5]

    context = {
        "boards": boards,
        "time_work": time_work,
        "updated_time": datetime.datetime.now(),
    }

    return render(request, "dashboard.html", context)


# 처음 로그인 페이지
def login(request):
    return render(request, "login.html")
