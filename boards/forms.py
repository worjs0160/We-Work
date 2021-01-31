from django import forms
from boards import models


class BoardForm(forms.ModelForm):

    attachments = forms.FileField(required=False)

    class Meta:
        model = models.Board
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
        model = models.Board
        fields = ["title", "contents"]

    def __init__(self, *args, **kwargs):
        super(UpdateBoardForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["placeholder"] = "제목을 입력해주세요"
        self.fields["title"].widget.attrs["style"] = "width: 50%"

    def save(self, *args, **kwargs):
        board = super().save(commit=False)
        return board


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = models.Comment
        fields = ["contents"]
        widgets = {
            "contents": forms.widgets.Textarea(attrs={
                'rows': 2,
                'cols': 80}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["contents"].widget.attrs["placeholder"] = "댓글을 입력해주세요"
