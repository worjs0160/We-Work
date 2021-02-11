from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from . import forms, models


def main(request):
    """ 전자결재 메인페이지 View """
    return render(request, "approvals/main.html")


def doc_format(request, doc):
    """
    doc의 string 인자로 파일 이름값을 받아
    approvals/doc_format/ 에 있는 해당 doc를 render로 반환
    """
    if doc == "draft.html":
        form = forms.DraftForm()

    elif doc == "voucher.html":
        form = forms.VoucherForm()

    elif doc == "result.html":
        form = forms.ResultForm()

    elif doc == "meeting.html":
        form = forms.MeetingForm()

    elif doc == "business.html":
        form = forms.BusinessForm()

    return render(request, "approvals/doc_format/" + doc, {"form": form})


def new_doc(request):
    return render(request, "approvals/partials/new_doc.html")


@login_required
def createDocView(request):

    doctype = request.POST.get("doctype")
    create_template = "approvals/main.html"
    print("문서타입: " + doctype)

    if doctype == "draft":
        form = forms.DraftForm(request.POST or None)
    elif doctype == "business":
        form = forms.BusinessForm(request.POST or None)
    elif doctype == "meeting":
        form = forms.MeetingForm(request.POST or None)
    elif doctype == "voucher":
        form = forms.VoucherForm(request.POST or None)
    elif doctype == "result":
        form = forms.ResultForm(request.POST or None)
    else:
        return render(request, create_template)

    if request.method == "POST":
        if form.is_valid():
            approval = form.save()
            approval.author = request.user
            approval.status = "request"
            approval.save()
            form.save_m2m()
            return redirect(reverse("approvals:main"))

        else:
            # 입력된 폼이 유효하지 않은 경우
            print("폼이 유효하지 않음")
            print(form.errors)
            # return render(request, create_template, {"form": form})
            return redirect(reverse("approvals:main"))

    else:
        return render(request, create_template, {"form": form})


@login_required
def ListMyDocView(request):

    a_draft = models.Draft.objects.filter(author=request.user)
    a_meeting = models.Meeting.objects.filter(author=request.user)
    a_business = models.Business.objects.filter(author=request.user)
    a_result = models.Result.objects.filter(author=request.user)
    a_voucher = models.Voucher.objects.filter(author=request.user)

    context = {
        "a_drafts": a_draft,
        "a_meetings": a_meeting,
        "a_business": a_business,
        "a_results": a_result,
        "a_vouchers": a_voucher,
    }

    return render(request, "approvals/my_doc_list.html", context)


def DetailView(request):
    def get(self):
        doc_id = self.request.GET.get("pk")
        print(doc_id)

    return render(request, "approvals/doc_detail.html")