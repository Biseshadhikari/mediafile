from django.shortcuts import render
from .forms import *
# Create your views here.



def home(request): 
    todolists = TodolistForm()
    context = { 
               'forms':todolists
            }
    return render(request,'index.html',context)