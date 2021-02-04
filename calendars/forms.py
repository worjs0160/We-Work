from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from calendars.models import Calendar

class EventForm(BSModalModelForm):

    attached_file = forms.FileField(required=False)

    class Meta:
        model = Calendar
        widgets = {
            "start_time": forms.DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "end_time": forms.DateInput(
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
        
    # 종료일이 시작일보다 과거이면 오류출력.
    def clean(self):
        start_time = self.cleaned_data.get("start_time")
        end_time = self.cleaned_data.get("end_time")
        if start_time > end_time:
            self.add_error("end_time",forms.ValidationError("종료일 시간이 잘못되었습니다."))
        else:
            return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)
