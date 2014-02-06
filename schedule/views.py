import json
from django.shortcuts import render
from django.http import HttpResponse
import itertools
from operator import itemgetter
from schedule.models import Choices
from django.views.decorators.http import require_http_methods

import pprint
pp = pprint.PrettyPrinter(indent=4)



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

def sched(req):
    objects = Choices.objects.all().iterator()
    dicted = [{'day': choice.day, 'block_length': choice.block_length, 'block_start': choice.block_start} for choice in objects]
    something = []
    for x in dicted:
        start = x['block_start']
        stop = start + x['block_length']
        for i in range(start, stop):
            something.append('{} {}'.format(x['day'], i))
    return  HttpResponse(json.dumps({'data': something}))

@require_http_methods(["GET", "POST"])
def updatesched(req):
    if req.method == 'POST':
        data = json.loads(req.POST.get('tabledata'))
        days = itertools.groupby(sorted(data), lambda x: x[0] )
        weds = []
        for k,g in days:
            if k == 'Wednesday':
                pp.pprint(type(g))
                weds.append(list(g))
        print 'd'
        mapeed = map(lambda x: x[1], [item for sublist in weds for item in sublist])
        for k, g in itertools.groupby(enumerate(mapeed), lambda (i,x):i-x):
            print map(itemgetter(1), g)
        #for k, g in days:
        #    pp.pprint(k)
        #    pp.pprint(list(g))
        return  HttpResponse(json.dumps(weds))
