from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return HttpResponse('Logged In!')
            else:
                return HttpResponse('Incorrect credentials!')

    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })