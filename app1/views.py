from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1(request):
    return render(request,'app1_first.html')

def app1_first(request):
    return HttpResponse('<center><h1>this the app1 first response</h1></center>')