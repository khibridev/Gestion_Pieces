from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

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

@login_required
def changer_password(request):
    if request.method == 'POST':
        ancien = request.POST.get('ancien_password')
        nouveau = request.POST.get('nouveau_password')
        confirmer = request.POST.get('confirmer_password')

        if not request.user.check_password(ancien):
            messages.error(request, '❌ Ancien mot de passe incorrect !')
        elif nouveau != confirmer:
            messages.error(request, '❌ Les mots de passe ne correspondent pas !')
        elif len(nouveau) < 6:
            messages.error(request, '❌ Le mot de passe doit avoir au moins 6 caractères !')
        else:
            request.user.set_password(nouveau)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, '✅ Mot de passe changé avec succès !')
            return redirect('profil')
    return render(request, 'accounts/changer_password.html')