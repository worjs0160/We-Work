import os
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse_lazy
from django.shortcuts import render, reverse, redirect, get_object_or_404
from . import forms
from . import models


def readBoardList(request):
    boards = models.Board.objects.all()
    return render(request, "boards/board_list.html", {"boards": boards})


def detailBoardView(request, pk):

    board = models.Board.objects.get(postNo=pk)
    return render(request, "boards/board_detail.html", {"board": board})


# Board delete
def deleteBoardView(request, pk):
    board = models.Board.objects.get(pk=pk)
    board.delete()
    return redirect(reverse("boards:board_list"))


def createBoardView(request):

    # 게시글 form POST 처리
    if request.method == "POST":
        form = forms.BoardForm(request.POST or None)

        if form.is_valid():
            board = form.save()
            board.author = request.user
            board.save()
            file = request.FILES.get("attachments")
            print(file)
            if file:
                models.Attachment.objects.create(file=file, board=board)
            else:
                models.Attachment.objects.create(board=board)
        return HttpResponseRedirect(reverse("boards:detail", kwargs={"pk": board.pk}))

    # 게시글 생성 GET 메소드 처리
    else:
        form = forms.BoardForm()
        return render(request, "boards/board_create.html", {"form": form})


def updateBoardView(request, pk):
    """Board Update"""

    board = get_object_or_404(models.Board, pk=pk)

    if request.method == "POST":
        form = forms.BoardForm(request.POST, instance=board)

        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            # 수정 시 파일 변경 및 삭제 처리 필요
            # file = request.FILES.get("attachments")
            # models.Attachment.objects.create(file=file, board=board)
        return HttpResponseRedirect(reverse("boards:detail", kwargs={"pk": board.pk}))

    else:
        title = board.title
        contents = board.contents

        if board.attachments.get(board=board).file.name:
            attachments = models.Attachment.objects.get(board=board)
            print("asdasda")

            form = forms.BoardForm(
                initial={
                    "title": title,
                    "contents": contents,
                    "attachments": attachments,
                }
            )
        else:
            form = forms.BoardForm(initial={"title": title, "contents": contents})

        return render(
            request,
            "boards/board_update.html",
            {"form": form, "board_pk": board.pk},
        )


"""-----------------댓글----------------"""


def createComment(request, pk):
    """댓글 생성"""

    if request.method == "POST":
        board = get_object_or_404(models.Board, pk=pk)
        contents = request.POST.get("contents")
        author = request.user

        models.Comment.objects.create(author=author, contents=contents, board=board)
        return render(request, "boards/board_detail.html", {"board": board})


def deleteComment(request, pk):
    """댓글 삭제"""
    comment = models.Comment.objects.get(pk=pk)
    board = comment.board
    comment.delete()
    return render(request, "boards/board_detail.html", {"board": board})


"""--------다운로드 함수---------"""


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
