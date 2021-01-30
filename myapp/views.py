

# Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

import requests
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
#from django.contrib.auth.models import Team
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import  CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)



@login_required(login_url='login')
def home(request):
	teams= Team.objects.all()
    
	total_teams= teams.count()
	'''
	orders = Order.objects.all()
	

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
    '''
	context = { 'teams':teams,
	'total_teams':total_teams }

	return render(request, 'index.html', context)


@login_required(login_url='login')
def calculate(request):
	teams= Team.objects.all()
    
	total_teams= teams.count()
	teammnumber=0
	hours=0
	calc_electricity=0
	calc_water=0
	calc_paper=0
	calc_ewaste=0
	calc_packaging=0
	calc_paper_waste=0
	total_footprint=0
	context={}


	if request.method == 'POST':
		#if request.POST.get('submits'):
		#print("hello")
		projectname=request.POST.get('projectname')
		teammnumber=int(request.POST.get('teammnumber'))
		hours=int(request.POST.get('hours'))
		paper=int(request.POST.get('paper'))
		ewaste=int(request.POST.get('ewaste'))


		electicity_usage_factor = 0.2832
		water_usage_factor = 0.0006
		ewaste_usage_factor = 0.0004
		packaging_usage_factor = 0.0001
		paper_usage_factor = 0.0028
		paper_waste_usage_factor = 0.0001

		calc_electricity = teammnumber*hours*electicity_usage_factor
		calc_water = teammnumber*hours*water_usage_factor
		calc_paper = teammnumber*hours*paper*paper_usage_factor
		calc_ewaste = teammnumber*hours*ewaste*ewaste_usage_factor
		calc_packaging = teammnumber*hours*packaging_usage_factor
		calc_paper_waste = teammnumber*hours*paper*paper_waste_usage_factor
        
        total_footprint=calc_electricity+calc_water+calc_paper+calc_ewaste+calc_packaging+calc_paper_waste
		
		context = { 'teams':teams,'total_members':teammnumber ,'hours':hours,
				'calc_electricity':calc_electricity,'calc_water':calc_water,'calc_paper':calc_paper,
				'calc_packaging' : calc_packaging , 'calc_paper_waste':calc_paper_waste,
				'calc_ewaste':calc_ewaste,'total_footprint':total_footprint }
		
	print(context)
	return render(request, 'calculator.html', context)

		

@login_required(login_url='login')
def checklist(request):
	teams= Team.objects.all()
    
	total_teams= teams.count()
	'''
	orders = Order.objects.all()
	

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
    '''
	context = { 'teams':teams,
	'total_teams':total_teams }

	return render(request, 'checklist.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
