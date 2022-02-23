from django.http import HttpResponse
from django.shortcuts import render
import json
import urllib.parse
import pymongo
#from rest_framework import viewsets
def searchmongo(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/vsj")
    dbname=client["vsj"]
    collection_name = dbname["vsj"]
    result = collection_name.find()
    print(result)
    a = list(result)
    print(a)
    a = a[0]
    js = json.dumps(a)
    return HttpResponse("Search " + str(js));
def hello(request):
    data={}
    return render(request, "hello.html", {'data':data})
def index(request):
    return HttpResponse("Welcome")
