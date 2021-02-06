from django import forms
from . import models

base_filds = ("author", "title", "contents", "viewer")


class DraftForm(forms.Form):
    class Meta:
        model = models.Draft
        fields = base_filds


class MeetingForm(forms.Form):
    class Meta:
        model = models.Meeting
        fields = base_filds


class BusinessForm(forms.Form):
    class Meta:
        model = models.Business
        fields = base_filds


class ResultForm(forms.Form):
    class Meta:
        model = models.Result
        fields = base_filds


class VoucherForm(forms.Form):
    class Meta:
        model = models.Voucher
        fields = base_filds