from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def portafolio_index(request):
    return HttpResponse("hello word")

def main_dashboard(request): 
    return render(request,"main_dashboard.html")