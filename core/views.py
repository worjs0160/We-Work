from django.shortcuts import render


def test_home(request):
    return render(request, "index.html")


def sample(request):
    return render(request, "sample.html")


def get_start(request):
    return render(request, "start_login.html")
