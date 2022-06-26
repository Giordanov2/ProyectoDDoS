from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from  django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import CreateUserForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('user')
                messages.success(request, 'Cuenta creada exitosamente!') 
                return redirect('login')

        context = {'form': form}
        return render(request,'analisis/register.html', context)    

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)    

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Usuario o contraseña incorrecta')
        context = {}
        return render(request,'analisis/login.html', context)   

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'analisis/home.html')

@login_required(login_url='login')
def editProfile(request):
    return render(request, 'analisis/editprofile.html')
