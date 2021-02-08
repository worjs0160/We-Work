
import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from boards import models


# 홈페이지 로딩
@login_required
def home(request):
    boards = models.Board.objects.order_by("-updated")[:5]
    return render(request, "dashboard.html", {"boards": boards})


# 처음 로그인 페이지
def login(request):
    return render(request, "login.html")

