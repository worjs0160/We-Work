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

    def __init__(self, *args, **kwargs):
        super(DraftForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["viewer"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["contents"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )


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

    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["viewer"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["start_date"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["end_date"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["place"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "80px",
                "rows": "2px",
                "style": "resize:none",
            }
        )
        self.fields["departments"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["agenda"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "80px",
                "rows": "5px",
                "style": "resize:none",
            }
        )
        self.fields["result"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "80px",
                "rows": "5px",
                "style": "resize:none",
            }
        )
        self.fields["etc"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "80px",
                "rows": "5px",
                "style": "resize:none",
            }
        )


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

    def __init__(self, *args, **kwargs):
        super(BusinessForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["viewer"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["d_goal"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "80px",
                "rows": "5px",
                "style": "resize:none",
            }
        )
        self.fields["w_goal"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "80px",
                "rows": "5px",
                "style": "resize:none",
            }
        )
        self.fields["last_do"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "80px",
                "rows": "5px",
                "style": "resize:none",
            }
        )
        self.fields["to_do"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "80px",
                "rows": "5px",
                "style": "resize:none",
            }
        )
        self.fields["priority"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "80px",
                "rows": "5px",
                "style": "resize:none",
            }
        )


class ResultForm(forms.ModelForm):
    class Meta:
        model = models.Result
        fields = base_fields
        widgets = {
            "contents": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["viewer"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["contents"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )


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

    def __init__(self, *args, **kwargs):
        super(VoucherForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["viewer"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["contents"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
        self.fields["usedby_d"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
                "cols": "50px",
                "rows": "1px",
                "style": "resize:none",
            }
        )
        self.fields["usedby_u"].widget.attrs.update(
            {
                "class": "input",
                "readonly": "true",
                "disabled": "true",
            }
        )
