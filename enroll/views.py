from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .models import AddJob,Info,Apply
from .forms import Addjob,Formaplly,Companyinfo
from .forms import Signup,Loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
# Create your views here.
def base(request):
    
    return render (request,'enroll/base.html')


#home views 
def home(request):
    return render(request,'enroll/home.html')



# login views form
def user_login(request):
   if not request.user.is_authenticated:
    if request.method=="POST":
        form=Loginform(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            pwd=form.cleaned_data['password']
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
            messages.info(request,'you have been loged in successfully')
            return HttpResponseRedirect('/login/')
    else:
            form=Loginform()
    return render(request,'enroll/login.html',{'form':form})
   else:
       return HttpResponseRedirect('/carear/')






#signup form views
def signup(request):
    if request.method=="POST":
        form=Signup(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations you have been registered')
            user=form.save()
            group=Group.objects.get(name='author')
            user.groups.add(group)
    else:
        form=Signup()
    return render (request,'enroll/signup.html',{'form':form})



#loguot views
def user_logout(request):
   
   logout(request)
   return HttpResponseRedirect('/login/')





#apply on jobs
def apply(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=Formaplly(request.POST)
            if form.is_valid():
                form.save()
        else:
            form=Formaplly()
        return render (request,'enroll/apply.html',{'form':form})
    else:
        return HttpResponseRedirect ('/login/')



#edit job details
def openings(request):
    if request.user.is_authenticated:
        jobs=AddJob.objects.all()
        company_details=Info.objects.all()
        return render(request,'enroll/openings.html',{'jobs':jobs,'company_details':company_details})
    return HttpResponseRedirect('/login/')



# hiring 
def addjob(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=Companyinfo(request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm=Companyinfo()
        if request.method=="POST":
            form=Addjob(request.POST)
            if form.is_valid():
                form.save()
        else:
            form=Addjob()
        return render(request,'enroll/addjob.html',{'form':form,'fm':fm})
    else:
        return HttpResponseRedirect('/login/')

def applications(request):
    if request.user.is_authenticated:
        form=Apply.objects.all()
        return render(request,'enroll/applications.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    

def editjob(request):
    if request.user.is_authenticated:
        return render(request,'enroll/edit.html')
    else:
        return HttpResponseRedirect('/login/')
    
def deletejob(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=AddJob.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/carear/')
    else:
        return HttpResponseRedirect('/login/')


