import json
from django.shortcuts import render
from django.http import HttpResponse
import itertools
from schedule.models import Choices
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
blocks = range(24)
props = [["{} {}".format(day, block) for day in days[2:4] for block in blocks[11:16]]]
chain = list(itertools.chain(*props))
def index(req):
    payload = {
        'days': days,
        'blocks': blocks
    }
    return render(req, 'schedule/index.html', payload)

from restless.views import Endpoint
from django.core import serializers

class scheduledata(Endpoint):
    def get(self, req):
        objects = Choices.objects.all().iterator()
        dicted = [{'day': choice.day, 'block_length': choice.block_length, 'block_start': choice.block_start} for choice in objects]
        something = []
        for x in dicted:
            start = x['block_start']
            stop = start + x['block_length']
            for i in range(start, stop):
                something.append('{} {}'.format(x['day'], i))
        return {'data': something}
