

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'microphone/home.html')
