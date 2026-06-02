from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Client

admin_only = user_passes_test(lambda u: u.is_staff, login_url='/login/')

@login_required
@admin_only
def liste_clients(request):
    query = request.GET.get('q', '')
    clients = Client.objects.all()
    if query:
        clients = clients.filter(
            nom__icontains=query
        ) | clients.filter(
            prenom__icontains=query
        ) | clients.filter(
            email__icontains=query
        ) | clients.filter(
            cin__icontains=query
        )
    return render(request, 'clients/liste.html', {'clients': clients, 'query': query})

@login_required
@admin_only
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

@login_required
@admin_only
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

@login_required
@admin_only
def supprimer_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('liste_clients')

@login_required
@admin_only
def detail_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/detail.html', {'client': client})