from django.forms import ModelForm
from .models import *
from django import forms
class TodolistForm(ModelForm): 
    class Meta: 
        model = Todolist
        fields = '__all__'
        widgets = { 
                   'title':forms.TextInput(attrs={
                       'class': '',
                       
                   })
                   }