import json

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
    def get(self,request):
        # self.loginname=request.COOKIES.get('myloginname','')
        # if self.loginname:
        #     return HttpResponse(self.loginname)
        # else:
        return render(request,'login.html')
    def post(self,request):
        self.loginname=request.POST['loginname']
        self.password=request.POST['password']
        uname=Accountinfo.objects.filter(username=self.loginname)
        upwd=Accountinfo.objects.filter(password=self.password)
        userId=Accountinfo.objects.get(username=self.loginname).id
        # self.remember=request.POST.get('remember','')
        params = {"resp": 0, "name": self.loginname}
        if uname and upwd:
            # resp = HttpResponse("1")
            # request.session['user']={"unane":self.loginname}
            # if self.remember == "1":
            #     resp.set_cookie("myloginname", self.loginname)
            params["resp"]=1
            return HttpResponse(json.dumps(params))
            # else:
            #     resp.delete_cookie('myloginname')
            #     return resp
        else:
            return HttpResponse(json.dumps(params))







