# projects/forms.py

from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']

        # Используем виджет для поля start_date с выпадающим окном
        start_date = forms.DateTimeField(
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # для выбора даты и времени
            required=True
        )

        # Используем виджет для поля start_date с выпадающим окном
        end_date = forms.DateTimeField(
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # для выбора даты и времени
            required=True
        )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'status', 'priority', 'assignee']
