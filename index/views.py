from django.shortcuts import render

# Create your views here.


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