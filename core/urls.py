from django.urls import path
from core.views import *
urlpatterns = [
     path("",home,name = "home"),
     path('create',create,name="create"),
     path("update/<int:id>",updateform,name = "updateform")
]
