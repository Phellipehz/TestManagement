from django.shortcuts import render

from django.shortcuts import render
from .models import Project

def index(request):
    items = Project.objects.all()
    return render(request, 'nomedoapp/index.html', {'items': items})