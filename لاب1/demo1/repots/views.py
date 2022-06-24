from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def liststudent(req):
    return HttpResponse('list students ')
def insertliststudents(req):
    return HttpResponse('insrted ')
