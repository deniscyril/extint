# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from members.forms import RegisterForm, LoginForm
from members.models import Profile


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data["username"]
            password = form.data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('projects.views.home'))
            else:
                error = u'Les identifiants fornis ne sont pas valides'
        else:
            error = u'Veuillez entrer vos identifiants'
    else:
        form = LoginForm()
    return render(request, 'members/login.html', {'form': form})
            
    
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():         
            first_name = form.data["first_name"]
            last_name = form.data["last_name"]
            username = form.data["username"]
            password = form.data["password"]
            email = form.data["email"]
            
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
            user.save()
            login(request, user)
            
            date_of_birth = form.data["date_of_birth"]
            #country = form.data["country"]
            country = "France"
            phone1 = form.data["phone1"]
            phone2 = form.data["phone2"]
            phone3 = form.data["phone3"]
            
            profile = Profile(user=user, date_of_birth=date_of_birth, country=country, phone1=phone1, phone2=phone2, phone3=phone3)     
            
            return render(request, 'members/register_success.html')
    else:
        form = RegisterForm()
    return render(request, 'members/register.html', {'form': form})
    
def edit_profile(request):
    pass
    
