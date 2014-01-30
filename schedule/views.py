from django.shortcuts import render
from django.http import HttpResponse
from models import Person
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
def index(req):
  people = [{'id': 1, 'name' : 'foo'}, {'id': 2, 'name' : 'bar'}]
  return render(req, 'schedule/index.html', {'days':days, 'distance': range(10), 'special': [[1,2,4], [4,5,6]], 'people': Person.objects.all()})


