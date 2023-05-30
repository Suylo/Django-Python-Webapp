from django.shortcuts import render, redirect

from connexion.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !!')
            return redirect('pizzas')
    else:
        form = UserRegistrationForm()
    return render(request, 'connexion/register.html', {'form': form})