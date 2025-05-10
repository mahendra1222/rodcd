from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>🎉 Happy New Year! 🎉 Mahendra Reddy Gangasani </h1>")

