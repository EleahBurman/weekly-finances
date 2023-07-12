from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Weekly Finances</h1>')

def bio(request):
  return render(request, 'bio.html')
