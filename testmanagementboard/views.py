from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from .models import Project, TestCase, TestExecution, TestSuite, TestPlan


def index(request):
    return render(request, 'index.html')


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    testplans = TestPlan.objects.filter(project=project)
    testsuites = TestSuite.objects.filter(test_plan__in=testplans)
    testcases = TestCase.objects.filter(suite__in=testsuites)

    data = {
        'project': project,
        'testplans': testplans,
        'testsuites': testsuites,
        'testcases': testcases
    }

    return render(request, 'project_detail.html', data)


###########################################################################


def design(request):
    test_cases = TestCase.objects.all()
    if "current_project" in request.session:
        project_id = request.session["current_project"]
    else:
        project_id = None
    return render(request, 'design.html', {'testcases': test_cases, 'project_id': project_id})


def report(request):
    return render(request, 'report.html')


def test(request):
    return render(request, 'test.html')


def test_case_list(request):
    testcases = TestCase.objects.all()
    return render(request, 'test_case_list.html', {'testcases': testcases})


"""
def update_test_step_status(request, test_step_id, new_status):
    if new_status in ['Certo', 'Erro']:
        #test_step.status = new_status
        #test_step.save()
        return JsonResponse({'success': True, 'message': f'Status atualizado para {new_status}.'})
    else:
        return JsonResponse({'success': False, 'message': 'Status inválido.'})
"""
