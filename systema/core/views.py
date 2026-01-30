from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Machine, Allocation, Student

@login_required(login_url='/auth/login')
def home(request):
    return render(request, 'core/home.html', { 'user': request.user, 'total_m_count': Machine.objects.count(), 'total_s_count': Student.objects.count(), 'good_pcs': Machine.objects.filter(condition="Good").count(), 'missing': Machine.objects.filter(condition="Missing").count() })

@login_required(login_url='/auth/login')
def signout(request):
    logout(request)
    return redirect('login')