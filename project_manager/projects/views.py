# projects/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm

# Страница с проектами
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

# Страница с задачами проекта
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})

# Создание проекта
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

# Создание задачи
def create_task(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'projects/create_task.html', {'form': form, 'project': project})
