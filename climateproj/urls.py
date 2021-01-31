

from django.conf.urls import *
from django.contrib import admin
from myapp import views
from django.views.generic import TemplateView
from django.urls import path
from myapp import views

'''
urlpatterns = [
    path('admin/', admin.site.urls),
]
'''

from django.views.generic import TemplateView



urlpatterns = [

	url(r'register', views.registerPage, name="register"),
	url(r'login', views.loginPage, name="login"),  
	url(r'logout', views.logoutUser, name="logout"),
    url(r'checklist', views.checklist, name="checklist"),
    url(r'calculate', views.calculate, name="calculate"),
    url(r'dashboard', TemplateView.as_view(template_name="dashboard.html"), name='dashboard'),
    #url(r'result', views.calculate,name="result"),



    url(r'home', views.home, name="home"),
   



]

