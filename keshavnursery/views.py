from django.shortcuts import render
from keshavnursery.models import *

# Create your views here.
def homeView(request):
	return render(request,'index.html')

def Areca(request):
	return render(request,'Areca_Palm.html')

def Dracaena(request):
	return render(request,'Dracaena.html')

def Ipomoea(request):
	return render(request,'Ipomoea.html')

def Italian(request):
	return render(request,'Italian_basil.html')

def Lavender(request):
	return render(request,'Lavender.html')

def Lemon(request):
	return render(request,'LemonCroton.html')

def Marigold(request):
	return render(request,'Marigold.html')

def Lily(request):
	return render(request,'Peace_Lily.html')

def Queen(request):
	return render(request,'Pothos_Marble_Queen.html')

def Rose(request):
	return render(request,'Rose.html')

def Indoor(request):
	return render(request,'Snake_Indoor.html')

def login(request):
	return render(request,'login.html')

def LoginView(request):
	data=Rgister.objects.all()
	name=request.GET['name']
	contact=request.GET['contact']
	for d in data:		
		if name == d.name and contact== d.contact:
			print('success')
			return render(request,'index.html')		
	return render(request,'login.html')
	#data=Login.objects.all();
	
def RegisView(request):
	return render(request,'registration.html')	

def RegView(request):
	data=Rgister()
	data.name=request.GET['name']
	data.contact=request.GET['contact']
	data.email=request.GET['email']
	data.save()
	data=Rgister.objects.all()
	return render(request,'login.html')
