from django.shortcuts import render
from django.http import HttpResponse
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
def index(req):
  return render(req, 'schedule/index.html', {'days':days, 'distance': range(10)})

