from django.shortcuts import render
from django . http import HttpResponse
import random


def home(request):
    return render(request,'a.html')


def about(request):
    return render(request,'about.html',{'link':'http://127.0.0.1:8000/'})


def nameee(request):
    g=request.POST['name1']
    return render(request,'b.html',{'t':g})

def expression(request):
    a =random.randint(1,10)
    b=request.POST['value1']
    try:
        c=int(b)
    except:
        j="invalid input"
        return render(request,'output.html',{'result':j})
        quit()
    if (a == c):
       n= "you win!!!!!!"
       return render(request, 'output.html',{'result':n})
    else:
         dare=["You lost!! and your dare is:dance like a kid","You lost!! and your dare is:sing in cat voice","You lost!! and your dare is:crack a joke","You lost!! and your dare is:do nothing"]
         op=random.choice(dare)
         return render(request,'output.html',{'result':op})
