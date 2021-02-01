from django.shortcuts import redirect, render, reverse


def paper_main(request):
    """ 전자결재 테스트 """
    return render(request, "papers/paper_main.html")
