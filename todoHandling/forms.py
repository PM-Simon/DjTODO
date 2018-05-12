from django import forms
from .models import TODO


class TodoForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deadline = forms.DateField()
    progress = forms.IntegerField()

    class Meta:
        model = TODO
        fields = ["title", "description", "deadline", "progress", ]