from django.shortcuts import render

from django.shortcuts import render
from .models import Project


def index(request):
    projects_count = Project.objects.count()
    context = {
        'projects_count': projects_count,
    }
    return render(request, 'index.html', context)


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})