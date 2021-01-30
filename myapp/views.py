

# Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

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
	'''
	orders = Order.objects.all()
	

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
    '''
	context = { 'teams':teams,
	'total_teams':total_teams }

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
