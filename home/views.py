from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts import models
from django.http import JsonResponse
from .models import sport,issued
import json
# Create your views here.
def ava(request):
    if request.method =="POST":
        whichSport=request.body
        whichSport=json.loads(request.body)
        avaliable=sport.objects.get(id=whichSport['sport']).ava
    return JsonResponse({'ava':avaliable})
@login_required(login_url="/login")
def home(request):
    data={}
    guard_access=models.CustomUser.objects.get(username=request.user).guard_access
    data['guard_access']=guard_access

    user = models.CustomUser.objects.get(username=request.user.username)

    if(guard_access==False ):
        all_val_user=issued.objects.filter(user=user)
        data['sendNotification']=all_val_user

    all_val=issued.objects.all()
    data["all_val"]=all_val
    print(all_val)
    
    return render(request,'home/home.html',data)
def issueEquipment(request):
    if request.method == 'POST':
        # Get the data from the form
        sport1 = request.POST.get('sport')
        availability = request.POST.get('availability')
        
        # Creating username istance
        user = models.CustomUser.objects.get(username=request.user.username)
        # Creating sport isnatnace
        sp = sport.objects.get(id=int(sport1))
        sp.ava-=1
        sp.save()
        creatingIssuing=issued.objects.create(user=user,sporting=sp,issued_number=int(availability))
        creatingIssuing.save()

        redirect('/')
    return render(request,'home/issue.html')