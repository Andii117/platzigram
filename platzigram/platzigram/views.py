#modulo para poner la hora
from datetime import date, datetime
from django.http import HttpResponse
import json

from django.http.response import ResponseHeaders


def hello_word(request):
    return HttpResponse('Hello Word!!!, oh hi, current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def hi(request):
    #servicio para usar el debuger
    #import pdb; pdb.set_trace()
    numbers = [int (i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data= {
        'status' : 'OK',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    #json.dumps convierte un diccionario (data) en formato json
    return HttpResponse(
            json.dumps(data), 
            content_type = 'application/json' 
            )

def say_hi(request, name, age):
    #retur a greating.

    if age<12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else: 
        message = 'Hi, {}, welcome to platzigram'.format(name)
    return HttpResponse(message)
