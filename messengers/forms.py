from django import forms


class Messege(forms.Form):

    message = forms.CharField(required=True, widget=forms.TextInput())
