from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseNotAllowed
from django.contrib.auth import authenticate,login,logout

import json
#Handle Json Response
def handleJsonlogin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username=data['username']
        password=data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return JsonResponse({'response':True},safe=False)
        else:
            return JsonResponse({'response':False,'error':'Username or Password is incorrect'}, safe=False)
    else:
        return HttpResponseNotAllowed(['POST'])

# Create your views here.
def login_(request):
    return render(request,'accounts/login.html')

def logout_(request):
    logout(request)
    return redirect('/login')