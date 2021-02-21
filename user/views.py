from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.forms import *
from user.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files import File
from django.template.loader import get_template
from user.convertor import StreamingConvertedPdf

# Create your views here.

def homeview(request):
    return render(request,'user/home.html')

def logoutview(request):
    return render(request,'user/logout.html')

def signupview(request):
    form=signupform()
    if request.method=='POST':
        form=signupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'user/signup.html',{'form':form})

def loginview(request):
    return render(request,'registration/login.html')
@login_required
def view_filefield(request):
    user = User.objects.get(id=request.user.id)
    choose = filefield.objects.filter(user=user)
    context = {'choose':choose}
    return render(request, 'user/1.html',context)


@login_required
def filefieldview(request,):
    form=filefieldForm()
    if request.method=='POST':
        form=filefieldForm(request.POST, request.FILES)
        if form.is_valid():
            ct = User.objects.filter(username=request.user.username).first()
            n = request.FILES['choosefile']
            a=filefield.objects.create(user=ct,choosefile=n)
            user=form.save()
            user.save()
            return HttpResponseRedirect('/convertpdf')
    return render(request,'user/filefield.html',{'form':form})


@login_required
def convertpdf(request):
    form = filefieldForm(request.POST, request.FILES)
    if form.is_valid():
        r_file = request.FILES['choosefile']
        inst = StreamingConvertedPdf(r_file)
        return inst.stream_content()
    return render(request,'user/2.html',{'form':form})
