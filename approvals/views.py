from django.shortcuts import redirect, render, reverse


def main(request):
    """ 전자결재 메인페이지 View"""
    return render(request, "approvals/main.html")
