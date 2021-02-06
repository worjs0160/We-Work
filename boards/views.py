import os
import urllib
import mimetypes
from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect, get_object_or_404
from . import forms
from . import models


@login_required
def readBoardList(request):
    boards = models.Board.objects.all()
    return render(request, "boards/board_list.html", {"boards": boards})


@login_required
def detailBoardView(request, pk):

    board = models.Board.get_or_none(postNo=pk)
    return render(request, "boards/board_detail.html", {"board": board})


# Board delete
@login_required
def deleteBoardView(request, pk):
    board = models.Board.objects.get(pk=pk)
    board.delete()
    return redirect(reverse("boards:board_list"))


@login_required
def createBoardView(request):

    create_template = "boards/board_create.html"
    # 게시글 생성 GET 메소드 처리
    if request.method == "GET":
        form = forms.BoardForm()
    
        return render(request, create_template, {"form": form})

    # 게시글 form POST 처리
    else:
        form = forms.BoardForm(request.POST or None)

        if form.is_valid():
            board = form.save()
            board.author = request.user
            board.save()
            
            file = request.FILES.get("attachments")
    
            if file:
                filename = file.name
                models.Attachment.objects.create(file=file, board=board, filename=filename)
            else:
                models.Attachment.objects.create(board=board)

            return HttpResponseRedirect(
                reverse_lazy("boards:detail", kwargs={"pk": board.pk})
            )

        else:
            #입력된 폼이 유효하지 않은 경우
            return render(request, create_template, {"form": form})

@login_required
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


@login_required
def createComment(request, pk):
    """댓글 생성"""

    if request.method == "POST":
        board = get_object_or_404(models.Board, pk=pk)
        contents = request.POST.get("contents")
        author = request.user

        models.Comment.objects.create(author=author, contents=contents, board=board)
        return render(request, "boards/board_detail.html", {"board": board})


@login_required
def deleteComment(request, pk):
    """댓글 삭제"""
    comment = models.Comment.objects.get(pk=pk)
    board = comment.board
    comment.delete()
    return render(request, "boards/board_detail.html", {"board": board})


# 다운로드
@login_required
def download(request, pk):
    attachment = get_object_or_404(models.Attachment, pk=pk)
    path = attachment.file.url[1:]
    filename = attachment.filename
    file_path = urllib.parse.unquote(path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            #urlib.parse.quote => utf-8 형식으로 filename 인코딩
            quote_file_url = urllib.parse.quote(filename.encode('utf-8'))
            # 파일의 확장자를 통해 mimetype을 결정해주는 guess_type
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(path)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
    raise Http404()
