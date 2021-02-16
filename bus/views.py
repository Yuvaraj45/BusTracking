from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import bus,track
from .forms import *
# Create your views here.
@login_required(login_url='blog:user_login')
def bus_list(request):
	obj = bus.objects.all()
	return render(request,'home.html',{'obj':obj})

def bus_detail(request,slug_text):
	obj = bus.objects.get(slug=slug_text)
	context = {
	'obj':obj,
	'track':track.objects.get(id=1)
	}
	return render(request,'postdetail.html',context)

def bus_track(request,slug_lat,slug_lng,slug_uid):
	a= track(id=1,lng=slug_lng,lat=slug_lat,uid=slug_uid)
	a.save()
	print(slug_lng,slug_lat,slug_uid)
	return HttpResponse("Done..")

def user_registration(request):
	form =  userregistration(request.POST or None)
	# profileform = userprofile(request.POST or None,request.FILES or None)
	if request.method == 'POST':
		if form.is_valid() and profileform.is_valid():
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			if password != confirm_password:
				raise forms.ValidationError("Password Mismatch ")
			newuser = form.save(commit=False)
			# profile = profileform.save(commit=False)
			newuser.set_password(password)
			newuser.save()
			# profile.save()
			return redirect("blog:buslist")
	context = {
				'form':form,
				'profileform':profileform
				}
	return render(request,'userregistration.html',context)

def user_login(request):
	if request.method == 'POST':
		username = request.POST['loginid']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect("blog:buslist")
		else:
			return HttpResponse("invalid account ")
	return render(request,'userlogin.html',{})

def user_logout(request):
	logout(request)
	return redirect("blog:buslist")




