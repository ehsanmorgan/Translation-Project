from django.shortcuts import render
from .models import Questions


def home(request):
   return render(request,"transaltion/home.html")


def test_translation(request):
   test=Questions.objects.all()
   return render(request,'test.html',{'test':test})