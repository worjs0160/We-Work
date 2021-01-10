from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from boards.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("title", "contents")

        widgets = {"contents": forms.CharField(widget=CKEditorUploadingWidget())}

    def save(self, *args, **kwargs):
        board = super().save(commit=False)
        return board
