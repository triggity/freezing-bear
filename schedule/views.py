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
        consecs = create_groupings(data)
        model_dicts = to_model_dicts(consecs)
        print dir(Choices.objects.all())
        Choices.objects.all().delete()
        map(dict_to_model, model_dicts)
        
        return  HttpResponse(json.dumps(consecs))
def dict_to_model(item):
    choice = Choices(**item)
    choice.save()
#returns a list of dictionarys representing model attributes
def to_model_dicts(data):
    models = [{'day': k, 'block_start': i[0], 'block_length': len(i) }  for (k, v) in data.iteritems() for i in v ]
    return models

def create_groupings(data):
    #takes response and parses it out into a series of lists by day
    days = itertools.groupby(sorted(data), lambda x: x[0] )
    by_day = {}
    for k,g in days:
        if k not in by_day:
            by_day[k] = []
        by_day[k].append(list(g))
    
    # takes input and flattens it
    by_day_flat = {day: flatten_list(values) for (day, values) in by_day.iteritems()}
    
    # plucking out the 'block' key into a list
    plucked_blocks = { day: map(lambda x: x[1], values) for (day, values) in by_day_flat.iteritems()}
    
    print 'consecs'
    # groups into consecutive integers
    consecs = { k: find_consecutive(v) for k, v in plucked_blocks.iteritems()}
    return consecs

# given a list of data, finds consecutive integers and returns a list of lists
def find_consecutive(data_list):
    grouped = itertools.groupby(enumerate(data_list), lambda (i,x):i-x)
    output = [map(itemgetter(1), g) for k, g in grouped]
    return output

def flatten_list(fat_list):
    return [item for sublist in fat_list for item in sublist]

#takes itertools grpoupby object and 
def by_day(data):
    pass
