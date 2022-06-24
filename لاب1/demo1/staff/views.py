from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json
# Create your views here.

def insert(request):
    res= HttpResponse()
    res.write('<center><h1> Hello From insert</h1></center>> ')

    return JsonResponse({'name': 'osman', 'id': 23})
def view(request):
    res= HttpResponse()
    res.write('<center><h1> welcom to  Staff Studnet</h1></center> ')
    return res
def update(request):
    res= HttpResponse()
    res.write('<center><h1>  welcom to  update</h1></center> ')
    return JsonResponse({'name': 'Mahmoud', 'id': 30})

def index(request):
    res = HttpResponse()
    res.write('<center><h1> Hello from Staff Index  </h1></center> ')
    return res

def delete(request):
    res = HttpResponse()

    return HttpResponseRedirect('../Staff/view')

