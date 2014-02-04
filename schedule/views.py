import json
from django.shortcuts import render
from django.http import HttpResponse
import itertools
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
blocks = range(24)
props = [["{} {}".format(day, block) for day in days[2:4] for block in blocks[11:16]]]
chain = list(itertools.chain(*props))
def index(req):
    payload = {
        'days': days,
        'blocks': blocks,
        'table_data': json.dumps(chain)
    }
    return render(req, 'schedule/index.html', payload)

from restless.views import Endpoint

class scheduledata(Endpoint):
    def get(self, req):
        name = 'michael'#request.params.get('name', 'World')
        return {'data': chain}
        #return {'message': 'Hello, %s!' % name}
