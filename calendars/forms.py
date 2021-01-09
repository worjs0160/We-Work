from django.forms import DateInput
from bootstrap_modal_forms.forms import BSModalForm
from calendars.models import Calendar
from django import forms


class EventForm(BSModalForm):
    class Meta:
        model = Calendar
        fields = [
            "title",
            "place",
            "schedule",
        ]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)
