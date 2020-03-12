from django.shortcuts import render
from .models import Job


def home(reqeust):
    return render(reqeust, 'main/index.html', {'jobs': Job.objects.all()})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')