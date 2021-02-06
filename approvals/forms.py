from django import forms
from . import models
from django_summernote.widgets import SummernoteWidget

base_filds = ("author", "title", "contents", "viewer")


class DraftForm(forms.Form):
    class Meta:
        model = models.Draft
        fields = base_filds
        widgets = {
            "contents": SummernoteWidget(),
        }


class MeetingForm(forms.Form):
    class Meta:
        model = models.Meeting
        fields = base_filds + (
            "start_date",
            "end_date",
            "departments",
            "place",
            "attendee",
            "agenda",
            "result",
            "etc",
        )
        widgets = {
            "contents": SummernoteWidget(),
        }


class BusinessForm(forms.Form):
    class Meta:
        model = models.Business
        fields = base_filds + (
            "d_goal",
            "w_goal",
            "last_do",
            "to_do",
            "priority",
        )
        widgets = {
            "contents": SummernoteWidget(),
        }


class ResultForm(forms.Form):
    class Meta:
        model = models.Result
        fields = base_filds
        widgets = {
            "contents": SummernoteWidget(),
        }


class VoucherForm(forms.Form):
    class Meta:
        model = models.Voucher
        fields = base_filds + (
            "usedby_d",
            "usedby_u",
        )
        widgets = {
            "contents": SummernoteWidget(),
        }