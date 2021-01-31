from django.shortcuts import render
from boards import models


# 홈페이지 로딩
def test_home(request):
    boards = models.Board.objects.order_by("-updated")[:5]
    return render(request, "dashboard.html", {"boards": boards})


# 처음 로그인 페이지
def get_start(request):
    return render(request, "start_login.html")
