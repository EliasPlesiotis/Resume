from django.shortcuts import render
from django.core.mail import send_mail


def home(reqeust):
    return render(reqeust, 'main/index.html')
