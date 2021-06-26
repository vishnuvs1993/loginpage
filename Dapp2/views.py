from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vs(request):
    return HttpResponse("hello world")
def fuc(request):
    return render(request,'test.html')    