from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

def home(request):
	return render(request,"home.html",{})

def compiler(request):
	return render(request,"compiler.html",{})

def googleform(request):
	return render(request,"googleform.html",{})

def bankform(request):
	return render(request,"bankform.html",{})

def droplist(request):
	return render(request,"droplist.html",{})
