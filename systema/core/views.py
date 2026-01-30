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

@login_required(login_url='/auth/login')
def machine_list(request):
    if request.method == "GET":
        query = request.GET.get('q')
        machines = Machine.objects.filter(Q(name__icontains=query) | Q(condition__icontains=query)).order_by('-date_created') if query else Machine.objects.order_by('-date_created')
    else:
        machines = Machine.objects.order_by('-date_created')

    return render(request, 'core/machine_list.html', context={ 'machines': machines })

@login_required(login_url='/auth/login')
def add_machine(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('machines')
    
    else:
        form = MachineForm()

    return render(request, 'core/add_machine.html', context={ 'form': form })

@login_required(login_url='/auth/login')
def delete_pc(request, id):
   machine = get_object_or_404(Machine, pk=id)
   machine.delete()

   return redirect('machines')

@login_required(login_url='/auth/login')
def edit_pc(request, id):
    obj = get_object_or_404(Machine, pk=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        condition = request.POST.get('condition')

        obj.name = name
        obj.condition = condition

        obj.save()
        return redirect('machines')

    

    return render(request, 'core/edit_pc.html', {  'obj': obj })

def student_list(request):
    # TODO: Add seacrch functionality for student's list
    return render(request, 'core/student_list.html', { 'students': Student.objects.order_by('-date_created') })