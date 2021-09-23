from django.views import View
from django.shortcuts import render
# to take templates from texts, use render

class Home(View):
  def get(self,request):
    return render(request,"home.html", {})