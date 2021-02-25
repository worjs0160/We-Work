from django.db.models import Q
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.core import serializers
from users import models as user_models
from . import models
import json


def go_lobby(request):
    sender = request.user
    receiver = user_models.User.objects.all()
    return render(
        request,
        "messengers/lobby.html",
        {
            "sender": sender,
            "receiver": receiver,
        },
    )


def room(request, room_name):
    return render(request, "messengers/chatroom.html", {"room_name": room_name})


def go_room(request, pk1, pk2):
    sender = user_models.User.objects.get(pk=pk1)
    receiver = user_models.User.objects.get(pk=pk2)
    if sender is not None and receiver is not None:
        messenger = models.Messenger.objects.filter(participants=sender).filter(
            participants=receiver
        )
        if messenger.count() == 0:
            messenger = models.Messenger.objects.create()
            messenger.participants.add(sender, receiver)
            messenger = models.Messenger.objects.filter(participants=sender).filter(
                participants=receiver
            )
        room_pk = messenger.values("id")
        return render(
            request, "messengers/chatroom_test.html", {"room_pk": room_pk[0]["id"]}
        )