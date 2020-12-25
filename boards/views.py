from django.core.paginator import Paginator
from django.shortcuts import render
from . import models as board_models


# Board Read
def readBoardList(request):
    # Board 모델에 대한 Objects : all_board
    all_boards = board_models.Board.objects.all()

    # 10개씩 queryset을 보여줌
    paginator = Paginator(all_boards, 10)
    page_num = request.GET.get("page")

    # page_obj
    boards = paginator.get_page(page_num)

    context = {
        "boards": boards,
    }
    return render(request, "boards/board_list.html", context)


def readBoardDetail(request, pk):
    board = board_models.Board.objects.get(pk=pk)

    context = {
        "board": board,
    }
    return render(request, "boards/board_contents.html", context)
