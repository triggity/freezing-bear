import json
from django.shortcuts import render
from django.http import HttpResponse
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
blocks = range(24)
def index(req):
  props = [["{} {}".format(day, block) for day in days] for block in blocks]
  payload = {
      'days': days,
      'blocks': blocks,
      'table_data': json.dumps(props)
  }
  print props
  people = [{'id': 1, 'name' : 'foo'}, {'id': 2, 'name' : 'bar'}]
  return render(req, 'schedule/index.html', payload)


