from django.shortcuts import render
from django.http import HttpResponse
from models import Person
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
blocks = range(24)
def index(req):
  payload = {
      'days': days,
      'blocks': blocks,
      'people': Person.objects.all()
  }
  people = [{'id': 1, 'name' : 'foo'}, {'id': 2, 'name' : 'bar'}]
  return render(req, 'schedule/index.html', payload)


