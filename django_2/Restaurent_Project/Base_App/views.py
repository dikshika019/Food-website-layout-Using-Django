

# Create your views here.
from django.shortcuts import render 

def HomeView(request):
    return render(request, 'home.html')

def BookTableView(request):
    pass

def MenuView(request):
    pass

def AboutView(request):
    pass