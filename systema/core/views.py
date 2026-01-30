from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db.models import Q
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Machine, Allocation, Student

@login_required(login_url='/auth/login')
def home(request):
    return render(request, 'core/home.html', { 'user': request.user, 'total_m_count': Machine.objects.count(), 'total_s_count': Student.objects.count(), 'good_pcs': Machine.objects.filter(condition="Good").count(), 'missing': Machine.objects.filter(condition="Missing").count() })

@login_required(login_url='/auth/login')
def signout(request):
    logout(request)
    return redirect('login')

def machine_list(request):
    if request.method == "GET":
        query = request.GET.get('q')
        machines = Machine.objects.filter(Q(name__icontains=query) | Q(condition__icontains=query)) if query else Machine.objects.all()
    else:
        machines = Machine.objects.all()

    return render(request, 'core/machine_list.html', context={ 'machines': machines })

def add_machine(request):
    return render(request, 'core/add_machine.html')