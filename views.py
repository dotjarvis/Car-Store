from django.http import HttpResponse
from django.shortcuts import render

from . models import Store

def index(request):
    store=Store.object.all()
    return render(request,'index.html',{
        'store':store
    })
