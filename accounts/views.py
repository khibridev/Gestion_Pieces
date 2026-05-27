from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('dashboard_admin')
            else:
                return redirect('dashboard_client')
        else:
            error = "Nom d'utilisateur ou mot de passe incorrect"
    return render(request, 'accounts/login.html', {'error': error})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')