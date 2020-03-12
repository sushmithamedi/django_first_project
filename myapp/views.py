from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Congratulations!!! My first web page")
    # dict={'name:"This is my View'}
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is my about page")

def contact(request):
    return HttpResponse("contact us here")

