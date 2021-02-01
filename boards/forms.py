from django import forms
from boards import models
from django_summernote.widgets import SummernoteWidget


class BoardForm(forms.ModelForm):

    attachments = forms.FileField(required=False)

    class Meta:
        model = models.Board
        fields = ["title", "contents", "attachments"]
        widgets={
            "contents": SummernoteWidget(), 
        }

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["placeholder"] = "제목을 입력해주세요"
        self.fields["title"].widget.attrs["style"] = "width: 50%"
        self.fields["contents"].error_messages = {"required": "글이 너무 짧습니다. 10자 이상 입력해주세요."}

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("2자 이상 입력해주세요.(2자 ~ 80자 이내)")

        if len(title) > 80:
            raise forms.ValidationError("80자 이내로 입력해주세요.(2자 ~ 80자 이내)")
            
        return title

    def clean_contents(self):
        contents = self.cleaned_data.get('contents')
        print(contents)
        if not len(contents):
            raise forms.ValidationError("글이 너무 짧습니다. 10자 이상 입력해주세요.")

        return contents


    def save(self, *args, **kwargs):
        board = super().save(commit=False)
        return board


class UpdateBoardForm(forms.ModelForm):
    class Meta:
        model = models.Board
        fields = ["title", "contents"]

    def __init__(self, *args, **kwargs):
        super(UpdateBoardForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["placeholder"] = "제목을 입력해주세요"
        self.fields["title"].widget.attrs["style"] = "width: 50%"

    def save(self, *args, **kwargs):
        board = super().save(commit=False)
        return board

