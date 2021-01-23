from django.forms import DateInput
from bootstrap_modal_forms.forms import BSModalForm, BSModalModelForm
from calendars.models import Calendar
from django import forms
from . import models


class EventForm(BSModalModelForm):
    class Meta:
        model = Calendar
        widgets = {
            "start_time": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
        }
        fields = [
            "title",
            "place",
            "schedule",
            "start_time",
            "end_time",
            "attached_file",
        ]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)

    def save(self, *args, **kwargs):
        calendar = super().save(commit=False)
        return calendar
