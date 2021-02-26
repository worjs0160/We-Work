from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from calendars.models import Calendar

class EventForm(BSModalModelForm):
    file = forms.FileField(required=False)
    
    class Meta:
        model = Calendar
        widgets = {
            "start_time": forms.DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "end_time": forms.DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M",
            ),
        }
        fields = [
            "title",
            "place",
            "schedule",
            "start_time",
            "end_time",
            "file",
            "all_day",
        ]
        error_messages = {
            'title': {'required': "제목을 입력해주세요.(최대 20자)"},
            'place': {'required': "장소를 입력해주세요.(최대 20자)"},
            'schedule': {'required': "내용을 입력해주세요.(최대 100자)"},
            'start_time': {'required': "시작일을 선택해주세요."},
            'end_time': {'required': "종료일을 선택해주세요."},
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if len(title) > 15:
            self.add_error("title",forms.ValidationError("제목이 너무 깁니다.(최대 15자)"))
        return title

    def clean_place(self):
        place = self.cleaned_data.get("place")

        if len(place) > 50:
            self.add_error("place",forms.ValidationError("장소 이름이 너무 깁니다.(최대 50자)"))
        return place

    def clean_schedule(self):
        schedule = self.cleaned_data.get("schedule")

        if len(schedule) > 100:
            self.add_error("schedule",forms.ValidationError("내용이 너무 깁니다.(최대 100자)"))
        return schedule

    # 종료일이 시작일보다 과거이면 오류출력.
    def clean_end_time(self):
        start_time = self.cleaned_data.get("start_time")
        end_time = self.cleaned_data.get("end_time")

        if start_time > end_time:
            self.add_error("end_time",forms.ValidationError("종료일 시간이 잘못되었습니다."))
        return end_time


    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)
