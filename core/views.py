import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from boards.models import Board as board_models
from attendance.models import Attendance as attendance_models


# 홈페이지 로딩
def homepage(request):
    boards = board_models.objects.order_by("-updated")[:5]
    return render(request, "dashboard.html", {"boards": boards})


# 처음 로그인 페이지
def get_start(request):
    return render(request, "start_login.html")


# 다운로드
@login_required
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response["Content-Disposition"] = "inline; filename=" + os.path.basename(
                file_path
            )
            return response
    raise Http404()
