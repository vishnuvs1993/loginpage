from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vs(request):
    return HttpResponse("hello world")
def fuc(request):
    return render(request,'login.html')    
def home1(request):
    return render(request,'home.html') 
def about1(request):
    return render(request,'about.html')  
def products1(request):
    return render(request,'products.html')
def services1(request):
    return render(request,'services.html')
def msi1(request):
    return render(request,'msi gaming s1.html')
def msi2(request):
    return render(request,'msi gaming s2.html')    
def msi3(request):
    return render(request,'msi gaming s3.html')

def msi5(request):
    return render(request,'msi gaming s5.html') 
def contactus1(request):
    return render(request,'contact us.html')           
              