from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Client

# Liste des clients
@login_required
def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/liste.html', {'clients': clients})

# Ajouter un client
@login_required
def ajouter_client(request):
    if request.method == 'POST':
        Client.objects.create(
            nom=request.POST['nom'],
            prenom=request.POST['prenom'],
            email=request.POST['email'],
            telephone=request.POST['telephone'],
            cin=request.POST['cin'],
            type_societe=request.POST['type_societe'],
        )
        return redirect('liste_clients')
    return render(request, 'clients/ajouter.html')

# Modifier un client
@login_required
def modifier_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.nom = request.POST['nom']
        client.prenom = request.POST['prenom']
        client.email = request.POST['email']
        client.telephone = request.POST['telephone']
        client.cin = request.POST['cin']
        client.type_societe = request.POST['type_societe']
        client.save()
        return redirect('liste_clients')
    return render(request, 'clients/modifier.html', {'client': client})

# Supprimer un client
@login_required
def supprimer_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('liste_clients')

# Détail d'un client
@login_required
def detail_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/detail.html', {'client': client})