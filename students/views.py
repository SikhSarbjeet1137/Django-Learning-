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

def student_details(request,student_id):
    return HttpResponse(f"Student ID: {student_id}")

def home_page(request):
    students=[
        {'name': 'Aarav', 'course': 'iMCA', 'marks': 75},
    {'name': 'Sarbjeet', 'course': 'iMCA', 'marks': 82},
    {'name': 'Krishna', 'course': 'BCA', 'marks': 82},
    ]
    context={
        'student_name': 'Sarbjeet',
        'course': 'IMCA',
        'semester': 7,
        'students': students
    }
    return render(request,'home.html',context)