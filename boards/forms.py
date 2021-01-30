from django import forms
from boards.models import Board


class BoardForm(forms.ModelForm):

    attachments = forms.FileField(required=False)

    class Meta:
        model = Board
        fields = ["title", "contents", "attachments"]

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["placeholder"] = "제목을 입력해주세요"
        self.fields["title"].widget.attrs["style"] = "width: 50%"

    def save(self, *args, **kwargs):
        board = super().save(commit=False)
        return board


class UpdateBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["title", "contents"]

    def __init__(self, *args, **kwargs):
        super(UpdateBoardForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["placeholder"] = "제목을 입력해주세요"
        self.fields["title"].widget.attrs["style"] = "width: 50%"

    def save(self, *args, **kwargs):
        board = super().save(commit=False)
        return board
