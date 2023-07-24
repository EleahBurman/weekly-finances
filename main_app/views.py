from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse(request, 'accounts/index.html', {'accounts': accounts})

def bio(request):
  return render(request, 'bio.html')

class Account:
  self.bank = bank
  self.checking = checking
  self.saving = saving 
  
accounts = [
  Account('TD Bank', 2100.00, 1000.00),
  Account('Chase', 1500.00, 1000.00)
]