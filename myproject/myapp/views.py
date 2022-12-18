from enum import unique
from multiprocessing import context
import re
from typing import final
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

import requests

# Create your views here.
@csrf_exempt

@csrf_exempt
def index(request):
    response=requests.get(' https://blockchain.info/ticker').json()
    response1=response.keys()
    if request.method=='POST':
        data2= request.POST.get('country')
        data1=request.POST.get('bitc')
        data3=response[data2]
        print(type(int(data3['last'])))
        print(type(int(data1)))
        data4=int(data1)
        
        data4=data4*(data3['last'])
        print("sf")

        return render(request,"index.html",{'response':response,'response1':response1,'data':data4,'data1':data1})


    else:    

        return render(request,"index.html",{'response':response,'response1':response1})