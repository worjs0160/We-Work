from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from users.models import User
from boards.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("title", "contents")

        widgets = {"contents": forms.CharField(widget=CKEditorUploadingWidget())}

    def save(self, *args, **kwargs):
        # test용
        user = User.objects.get(user_id="hsh")
        board = super().save(commit=False)
        board.author = user
        board.save()

    # board.save()
