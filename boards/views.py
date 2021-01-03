from django.views.generic import FormView, UpdateView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, reverse, redirect, get_object_or_404
from . import forms
from . import models as board_models


def readBoardList(request):
    boards = board_models.Board.objects.all().order_by("-updated")
    return render(request, "boards/board_list.html", {"boards": boards})


# Board List Read using paginator
"""
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
"""


class BoardDetailView(DetailView):
    """Board Detail 보여주기"""

    model = board_models.Board
    context_object_name = "board"


# Board delete
def deleteBoard(request, pk):
    board = board_models.Board.objects.get(pk=pk)
    board.delete()

    return redirect(reverse("boards:board_list"))


class CreateBoardView(FormView):

    """Board create"""

    template_name = "boards/board_create.html"
    form_class = forms.BoardForm
    success_url = reverse_lazy("boards:board_list")

    def form_valid(self, form):
        user = self.request.user
        title = form.data.get("title")
        contents = form.data.get("contents")
        board_models.Board.objects.create(title=title, contents=contents, author=user)
        return HttpResponseRedirect(self.get_success_url())


class UpdateBoardView(UpdateView):
    """Board Update"""

    model = board_models.Board
    template_name = "boards/board_update.html"
    fields = (
        "title",
        "contents",
    )

    def get_success_url(self):
        return self.get_object().get_absolute_url()


def createComment(request, pk):
    if request.method == "POST":
        board = get_object_or_404(board_models.Board, pk=pk)
        contents = request.POST.get("contents")
        author = request.user

        board_models.Comment.objects.create(
            author=author, contents=contents, board=board
        )
        return HttpResponseRedirect(
            reverse_lazy("boards:board_detail", kwargs={"pk": pk})
        )


def deleteComment(request, pk):
    comment = board_models.Comment.objects.get(pk=pk)
    board = comment.board
    comment.delete()
    return redirect(reverse("boards:board_detail", kwargs={"pk": board.pk}))
