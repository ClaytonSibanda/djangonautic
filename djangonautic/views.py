from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return HttpResponse("about page")
    return render(request,"about.html")

def home(request):
    # return HttpResponse("home page")
    return render(request,"home.html")
