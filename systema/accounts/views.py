from django.shortcuts import render
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(username, password)

    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })