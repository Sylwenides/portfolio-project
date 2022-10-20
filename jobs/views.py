from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs} )

def MathGame(request):
    return render(request, 'jobs/MathGame.html')

def FruitsGame(request):
    return render(request, 'jobs/FruitsGame.html')

def Stopwatch(request):
    return render(request, 'jobs/Stopwatch.html')

def DrawingApp(request):
    return render(request, 'jobs/DrawingApp.html')
