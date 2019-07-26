from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from index.models import Accountinfo


def index(request):
    return render(request,'index.html')

def party(request):

    return render(request,'party.html')

def diary(request):
    return render(request,'diary.html')

def login(request):
    return render(request,'login.html')

def reg(request):
    return render(request,'reg.html')

def case(request):
    return render(request,'case.html')

def safety(request):
    return render(request,'safety.html')

class CollateLogin(View):
    def post(self,request):
        self.loginname=request.POST['loginname']
        self.password=request.POST['password']
        uname=Accountinfo.objects.filter(username=self.loginname)
        upwd=Accountinfo.objects.filter(password=self.password)

        if uname and upwd:
            return HttpResponse("1")
        return HttpResponse("0")





