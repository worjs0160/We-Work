from django.shortcuts import render
from . import models as board_models


def board_list(request):
    boards = board_models.Board.objects.all()
    return render(request, "boards/board_list.html", {"boards": boards})


def test(request):
    boards = board_models.Board.objects.all()
    return render(request, "boards/test.html", {"boards": boards})
