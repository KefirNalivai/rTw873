import json

from django.shortcuts import render
import psycopg2

from myapp1.forms import *


def index_page(request):
    i = 1
    p = inputsFields.objects.all()
    p.delete()
    for key, name in request.POST.items():
        if(key != 'csrfmiddlewaretoken' and key != 'submit'):

            p = inputsFields(id = i,data={'name': key, 'value': name})
            p.save()
            i = i + 1
    return render(request, 'index.html')


def out_page(request):
    p = inputsFields.objects.all()
    return render(request, 'uotput.html', {'data': p})
