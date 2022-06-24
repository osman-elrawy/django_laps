from django.shortcuts import render
from django.http import HttpResponse
from .models import trainee
from .models import courses
# Create your views here.

def  listtrainee (req):
    trainees= trainee.objects.all()
    for traineeess in trainees:
     print(trainee.id,trainee.courses ,trainee.barnch)
     context={}
     context['title']='list page'
    context['trainees']=trainees

    return render(req,'index.html' ,context)

def insert(re):
    
    # c=courses(name='javascript')
    # c.save()
    # t=trainee(  national=1222, name='osman' , faculty='iti')
    # t.courses=c
    # t.save()
    print(re.POST)
    trainee.objects.create( courses=courses.objects.get(id=1) )
    return render(re, 'insert.html')


def update (reqq):
    t= trainee.objects.get(id=2)
    t.name='elrawy'
    t.save()
    print(t.name)


    return render( reqq,"update.html")

    def delete(req):
        context = {}
        outtrainne = trainee.objects.all()
        context['title'] = 'delete of trainee'
        context['outtrainne'] = outtrainne
        if (req.method == 'GET'):
            return render(req, 'delete.html', context)
        else:
            idl = req.POST['id']
            trainee.objects.filter(id=idl).delete()
            return render(req, 'delete.html', context)

    return render(req,'delete.html')