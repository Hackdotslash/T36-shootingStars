

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
    '''
    current_user = request.user
    user = Team.objects.get(teamname=current_user)
    form = ProfileForm(instance=user)
    '''

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
        bus=int(request.POST.get('bus'))
        car=int(request.POST.get('car'))
        train=int(request.POST.get('train'))
        flight=int(request.POST.get('flight'))


        electicity_usage_factor = 0.2832
        water_usage_factor = 0.0006
        ewaste_usage_factor = 0.0004
        packaging_usage_factor = 0.0001
        paper_usage_factor = 0.0028
        paper_waste_usage_factor = 0.0001
        bus_factor = 0.0030
        train_factor = 0.0045
        flight_factor = 0.3597
        car_factor  = 0.1162



        calc_electricity = teammnumber*hours*electicity_usage_factor
        calc_water = teammnumber*hours*water_usage_factor
        calc_paper = teammnumber*hours*paper*paper_usage_factor
        calc_ewaste = teammnumber*hours*ewaste*ewaste_usage_factor
        calc_packaging = teammnumber*hours*packaging_usage_factor
        calc_paper_waste = teammnumber*hours*paper*paper_waste_usage_factor
        bus_footprint = teammnumber * bus_factor
        train_footprint = teammnumber * train_factor
        car_footprint = teammnumber * car_factor
        flight_footprint = teammnumber * flight_factor

        total_footprint = calc_electricity + calc_water + calc_paper + calc_ewaste + calc_packaging + calc_paper_waste + car_footprint+bus_footprint+train_footprint+flight_footprint
        total_footprint = int(total_footprint)
        
        
        context = { 'teams':teams,'total_members':teammnumber ,'hours':hours,
                'calc_electricity':calc_electricity,'calc_water':calc_water,'calc_paper':calc_paper,
                'calc_packaging' : calc_packaging , 'calc_paper_waste':calc_paper_waste,
                'calc_ewaste':calc_ewaste,'bus_footprint':bus_footprint,'train_footprint':train_footprint,
                'car_footprint':car_footprint,'flight_footprint':flight_footprint,  'total_footprint':total_footprint }
    

   # get_db_footprint = Team.objects.get(teamname=request.user)
    #get_db_footprint['teamfootprint']=total_footprint
    #get_db_footprint.save()
    #print(get_db_footprint)
    
   
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
