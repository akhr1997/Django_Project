from django.views import View
from django.shortcuts import render
# to take templates from texts, use render

class Home(View):
  def get(self,request):
    return render(request,"home.html", {})

class John(View):
  def get(self,request):
    return render(request,"john.html", {})

class Paul(View):
  def get(self,request):
    return render(request,"paul.html", {})

class George(View):
  def get(self,request):
    return render(request,"george.html", {})

class Ringo(View):
  def get(self,request):
    return render(request,"ringo.html", {})