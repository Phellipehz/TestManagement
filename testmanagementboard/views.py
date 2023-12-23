from django.shortcuts import render

from django.shortcuts import render
from .models import Project, Release
from django.http import JsonResponse


def index(request):
    projects_count = Project.objects.count()
    context = {
        'projects_count': projects_count,
    }
    return render(request, 'index.html', context)


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    data = {
        'project': project,
        'releases': project.releases.all(),
        'test_cases': project.test_cases.all()
    }
    return render(request, 'project_detail.html', data)

"""
def update_test_step_status(request, test_step_id, new_status):
    if new_status in ['Certo', 'Erro']:
        #test_step.status = new_status
        #test_step.save()
        return JsonResponse({'success': True, 'message': f'Status atualizado para {new_status}.'})
    else:
        return JsonResponse({'success': False, 'message': 'Status inválido.'})
"""