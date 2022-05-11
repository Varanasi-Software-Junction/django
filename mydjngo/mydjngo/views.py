import json

import pymongo
from django.http import HttpResponse
from django.shortcuts import render
from sqlalchemy import create_engine


# from rest_framework import viewsets
def searchmongo(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/vsj")
    dbname = client["vsj"]
    collection_name = dbname["vsj"]
    result = collection_name.find()
    print(result)
    a = list(result)
    print(a)
    a = a[0]
    js = json.dumps(a)
    return HttpResponse("Search " + str(js));


def hello(request):
    data = {}
    return render(request, "hello.html", {'data': data})

def add(request,a=0,b=0):
    return HttpResponse("Add " + str(a+b))
def many(request,d):
    print(d)
    return HttpResponse("Add " + str(a+b))

def index(request):
    return HttpResponse("Welcome")


def dataintables(request):
    data = {1: "One", 2: "Two", 3: "Three"}
    return render(request, "table.html", {'data': data})


def multipletables(request):
    data = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9]}
    return render(request, "multipletable.html", {'data': data})


def datafrommysql(request):
    sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/django')
    # sqlEngine = create_engine("mysql+pymysql://{userid}:{password}@localhost/{database}".format(userid="root",password="",database="scores"))
    dbConnect = sqlEngine.connect()
    data = sqlEngine.execute("select * from books")
    names = data.keys()
    return render(request, "mysqltable.html", {'data': data,'names':names})
