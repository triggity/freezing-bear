import json
from django.shortcuts import render
from django.http import HttpResponse
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
blocks = range(24)
props = [["{} {}".format(day, block) for day in days[2:4] for block in blocks[11:16]]]
def index(req):
  payload = {
      'days': days,
      'blocks': blocks,
      'table_data': json.dumps(props)
  }
  print props
  return render(req, 'schedule/index.html', payload)

def tableData():
  print 'here'
  return {data: props}
