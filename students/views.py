from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello Boy")
def hello(request, name):
    return HttpResponse(f"Hello, {name}!")
def about(request):
    return HttpResponse("This is the about page.")
def status_check(request):
    return HttpResponse("Request Successfull",status=200)