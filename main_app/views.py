from django.shortcuts import render
from django.http import HttpResponse

# import models
from .models import Cat

# Create your views here.
# In django these are called views but they act as controllers
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')


# CATS
def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'index.html', { 'cats': cats })


# Steps for adding new pages and routes
# 1. make a view function
# 2. Make an HTML page
# 3. Add a new path