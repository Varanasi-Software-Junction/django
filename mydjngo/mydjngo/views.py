from django.http import HttpResponse
from django.shortcuts import render
#from rest_framework import viewsets

def hello(request):
    data={}
    return render(request, "hello.html", {'data':data})
def index(request):
    return HttpResponse("Welcome");
