from django import forms
from . import models
from django_summernote.widgets import SummernoteWidget

base_fields = ("title", "contents", "viewer")


class DraftForm(forms.ModelForm):
    class Meta:
        model = models.Draft
        fields = base_fields
        widgets = {
            "contents": SummernoteWidget(),
        }

    def save(self, *args, **kwargs):
        approval = super().save(commit=False)
        return approval


class MeetingForm(forms.ModelForm):
    class Meta:
        model = models.Meeting
        fields = base_fields + (
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


class BusinessForm(forms.ModelForm):
    class Meta:
        model = models.Business
        fields = base_fields + (
            "d_goal",
            "w_goal",
            "last_do",
            "to_do",
            "priority",
        )
        widgets = {
            "contents": SummernoteWidget(),
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = models.Result
        fields = base_fields
        widgets = {
            "contents": SummernoteWidget(),
        }


class VoucherForm(forms.ModelForm):
    class Meta:
        model = models.Voucher
        fields = base_fields + (
            "usedby_d",
            "usedby_u",
        )
        widgets = {
            "contents": SummernoteWidget(),
        }