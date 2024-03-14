from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Msg

# Create your views here.
def create (request):
    if(request.method == 'GET'):
        return render(request,'index.html')
    else:
        username = request.POST['uname'] # we are getting this from userr 
        contact = request.POST['umobile']
        email = request.POST['uemail']
        msg = request.POST['umsg']

        m = Msg.objects.create(name=username, mobile= contact, email=email, msg=msg) # we are taking this from models
        m.save()

        return render(request,'index.html')
    

def dashboard (request):
    context = {} #we use later #this is blank dictionary (not set )
    m= Msg.objects.all()  # we are fetching all data 
    context['data'] =m # we are getting all data here from fetch
    #print(m)

    return render(request,'dashboard.html', context) 

def edit(request, sid):# without id we cannot use this #id must 
    if request.method == 'GET':
        m = Msg.objects.filter(id = sid)
        context ={} #object fetch first 
        context['data'] =m 
        return render(request,'edit.html', context)
    else:
        username = request.POST['uname'] # we are getting this from userr 
        contact = request.POST['umobile']
        email = request.POST['uemail']
        msg = request.POST['umsg']

    m = Msg.objects.filter(id = sid).update(name=username, email= email, mobile= contact, msg=msg) #model.object.filter and pass id within
    return redirect("/") #dashboard this is view 

def delete(request,did):# without id we cannot use this 
    m = Msg.objects.filter(id = did)
    m.delete()
    return redirect("/") #redirect to dashboard view 


    