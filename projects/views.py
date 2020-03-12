from django.shortcuts import render
from .models import Project

# Create your views here.

def proj(request):
    return render(request, 'main/proj.html', {'projects': Project.objects.all()})
