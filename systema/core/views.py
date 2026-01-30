from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Machine, Allocation, Student
from .forms import MachineForm

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
        machines = Machine.objects.filter(Q(name__icontains=query) | Q(condition__icontains=query)).order_by('-date_created') if query else Machine.objects.order_by('-date_created')
    else:
        machines = Machine.objects.order_by('-date_created')

    return render(request, 'core/machine_list.html', context={ 'machines': machines })

def add_machine(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('machines')
    
    else:
        form = MachineForm()

    return render(request, 'core/add_machine.html', context={ 'form': form })

def delete_pc(request, id):
   machine = get_object_or_404(Machine, pk=id)
   machine.delete()

   return redirect('machines')