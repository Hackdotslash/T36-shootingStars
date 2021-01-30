from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from myapp.models import Team


from django import forms



#from .models import Order


Team = get_user_model()

class CreateUserForm(UserCreationForm):
	class Meta:
		
		model = Team
		fields = ['username', 'password1', 'password2']