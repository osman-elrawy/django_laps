from django.http import HttpResponse,HttpResponseRedirect
def sayhey(req):
    return HttpResponse('hello osman plz be smart and patiant')

def login(req):
    return HttpResponseRedirect('back')
def back(req):
    return HttpResponse('redirect from home viwe')