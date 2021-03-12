from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def aboutPage(request):
    return render(request, 'about.html')