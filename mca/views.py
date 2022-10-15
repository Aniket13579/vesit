from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

def home(request):
	return render(request,"home.html",{})

def compiler(request):
	return render(request,"compiler.html",{})