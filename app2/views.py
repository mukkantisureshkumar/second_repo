from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2(request):
    return render(request,'app2_first.html')

def app2_first(request):
    return HttpResponse('<center><h1>this is on by using app2_first')