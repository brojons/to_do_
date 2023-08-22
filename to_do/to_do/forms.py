from django import forms
from .models import ToDoListModel

class ToDoForm(forms.ModelForm):
    task_uz = forms.CharField()
    task_en = forms.CharField(required=False)
    task_ru = forms.CharField(required=False)

    class Meta:
        model = ToDoListModel
        exclude = ('task',)
