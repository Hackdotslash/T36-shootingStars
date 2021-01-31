

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
    url(r'dashboard', views.dashboard, name="dashboard"),

    url(r'admin', admin.site.urls),
    url(r'dashboard', TemplateView.as_view(template_name="dashboard.html"), name='dashboard'),
    url(r'menu', TemplateView.as_view(template_name="menu.html"), name='menu'),
    url(r'checklists', TemplateView.as_view(template_name="checklist.html"), name='checklists'),
     url(r'checklists', TemplateView.as_view(template_name="checklist.html"), name='checklists'),
    url(r'index', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'main', TemplateView.as_view(template_name="home.html"), name='home'),
    #url(r'result', views.calculate,name="result"),


    
    url(r'home', views.home, name="home"),
    url(r'main', views.main, name="main"),
   



]

