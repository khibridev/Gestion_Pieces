from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Contrat

admin_only = user_passes_test(lambda u: u.is_staff, login_url='/login/')

@login_required
@admin_only
def liste_contrats(request):
    query = request.GET.get('q', '')
    contrats = Contrat.objects.all()
    if query:
        contrats = contrats.filter(
            numero__icontains=query
        ) | contrats.filter(
            client__nom__icontains=query
        ) | contrats.filter(
            client__prenom__icontains=query
        )
    return render(request, 'contrats/liste.html', {'contrats': contrats, 'query': query})

@login_required
@admin_only
def ajouter_contrat(request):
    from clients.models import Client
    clients = Client.objects.all()
    if request.method == 'POST':
        Contrat.objects.create(
            client_id=request.POST['client'],
            numero=request.POST['numero'],
            pack=request.POST['pack'],
            date_debut=request.POST['date_debut'],
            date_fin=request.POST['date_fin'],
            statut=request.POST['statut'],
            adresse_domiciliation=request.POST['adresse_domiciliation'],
        )
        return redirect('liste_contrats')
    return render(request, 'contrats/ajouter.html', {'clients': clients})

@login_required
@admin_only
def modifier_contrat(request, pk):
    from clients.models import Client
    contrat = get_object_or_404(Contrat, pk=pk)
    clients = Client.objects.all()
    if request.method == 'POST':
        contrat.client_id = request.POST['client']
        contrat.numero = request.POST['numero']
        contrat.pack = request.POST['pack']
        contrat.date_debut = request.POST['date_debut']
        contrat.date_fin = request.POST['date_fin']
        contrat.statut = request.POST['statut']
        contrat.adresse_domiciliation = request.POST['adresse_domiciliation']
        contrat.save()
        return redirect('liste_contrats')
    return render(request, 'contrats/modifier.html', {'contrat': contrat, 'clients': clients})

@login_required
@admin_only
def supprimer_contrat(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    contrat.delete()
    return redirect('liste_contrats')

@login_required
@admin_only
def detail_contrat(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    return render(request, 'contrats/detail.html', {'contrat': contrat})