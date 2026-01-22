from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login')
def home(request):
    return render(request, 'core/home.html', { 'user': request.user })

@login_required(login_url='/auth/login')
def signout(request):
    logout(request)
    return redirect('login')