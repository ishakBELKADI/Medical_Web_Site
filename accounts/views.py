from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Gérer la connexion réussie ici
            user=form.get_user()
            print(user.username)
            return render(request,'medcin.html',{'user':user})  # Rediriger vers la page d'accueil
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')