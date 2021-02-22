from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, SelectDateWidget


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'reminder']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            'reminder': SelectDateWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату и время'
            })
        }