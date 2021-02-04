from django.shortcuts import redirect, render, reverse


def main(request):
    """ 전자결재 메인페이지 View"""
    return render(request, "approvals/main.html")


def doc_format(request, doc):
    """
    doc의 string 인자로 파일 이름값을 받아
    approvals/doc_format/ 에 있는 해당 doc를 render로 반환
    """
    return render(request, "approvals/doc_format/"+doc)
