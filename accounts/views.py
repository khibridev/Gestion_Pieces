from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
@login_required
def profil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        return redirect('profil')
    return render(request, 'accounts/profil.html')
@login_required
def profil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        messages.success(request, '✅ Profil mis à jour avec succès !')
        return redirect('profil')
    return render(request, 'accounts/profil.html')