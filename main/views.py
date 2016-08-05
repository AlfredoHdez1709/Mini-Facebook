from django.shortcuts import render
from django.views.generic import View

class MainView(View):
	def get(self,request):
		template_name = 'inicio.html'
		return render(request,template_name)


# Create your views here.

