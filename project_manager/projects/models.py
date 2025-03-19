# projects/models.py

from django.db import models
from django.contrib.auth.models import User

# Модель проекта
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

# Модель задачи
class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Не начата'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES, default='not_started', max_length=20)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='medium', max_length=20)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

# Модель истории изменений задачи
class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.name} - {self.action}"
