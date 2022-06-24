from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse



def jeson(req):

    return JsonResponse({'name':'osman','id':1 })
