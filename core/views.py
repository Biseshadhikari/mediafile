from django.shortcuts import render,redirect
from .forms import *
# Create your views here.



def home(request): 
    todolists = Todolist.objects.all()
    context = { 
               'todolist':todolists
            }
    return render(request,'index.html',context)



def create(request): 
    todoform = TodolistForm()
    if request.method == "POST": 
        todolistform = TodolistForm(request.POST)
        if todolistform.is_valid():
            todolistform.save()
        return redirect('/create')
    context = { 
               'form':todoform
               }
    return render(request,'create.html',context)



def updateform(request,id): 
    todolist = Todolist.objects.get(id = id)
    todolistform = TodolistForm(instance=todolist)
    if request.method == "POST": 
        todolistform = TodolistForm(request.POST,instance = todolist)
        if todolistform.is_valid(): 
            todolistform.save()
        
    return render(request,'create.html',{
        'form':todolistform
    })