from django.shortcuts import render


def index(request):
    return render(request, "messengers/index.html", {})


def room(request, room_name):
    return render(request, "messengers/chatroom.html", {"room_name": room_name})
