from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Coding Encouragement! 🚀 Your journey to coding excellence starts here.")
