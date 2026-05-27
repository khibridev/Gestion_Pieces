from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clients.models import Client
from contrats.models import Contrat
from paiements.models import Paiement

@login_required
def dashboard_admin(request):
    # Statistiques
    total_clients = Client.objects.count()
    total_contrats = Contrat.objects.count()
    contrats_actifs = Contrat.objects.filter(statut='actif').count()
    contrats_expires = Contrat.objects.filter(statut='expire').count()
    contrats_en_attente = Contrat.objects.filter(statut='en_attente').count()
    total_paiements = Paiement.objects.count()
    paiements_payes = Paiement.objects.filter(statut='paye').count()
    paiements_impayes = Paiement.objects.filter(statut='impaye').count()
    contrats_resilies = Contrat.objects.filter(statut='resilie').count()
    paiements_en_attente = Paiement.objects.filter(statut='en_attente').count()
    
    # Derniers clients ajoutés
    derniers_clients = Client.objects.order_by('-date_inscription')[:5]
    
    # Derniers contrats
    derniers_contrats = Contrat.objects.order_by('-id')[:5]

    context = {
        'total_clients': total_clients,
        'total_contrats': total_contrats,
        'contrats_actifs': contrats_actifs,
        'contrats_expires': contrats_expires,
        'contrats_en_attente': contrats_en_attente,
        'total_paiements': total_paiements,
        'paiements_payes': paiements_payes,
        'paiements_impayes': paiements_impayes,
        'derniers_clients': derniers_clients,
        'derniers_contrats': derniers_contrats,
        'contrats_resilies': contrats_resilies,
        'paiements_en_attente': paiements_en_attente,

    }
    return render(request, 'dashboard/admin.html', context)

@login_required
def dashboard_client(request):
    # Contrats du client connecté
    try:
        client = Client.objects.get(email=request.user.email)
        contrats = Contrat.objects.filter(client=client)
        paiements = Paiement.objects.filter(contrat__client=client)
    except Client.DoesNotExist:
        contrats = []
        paiements = []

    context = {
        'contrats': contrats,
        'paiements': paiements,
    }
    return render(request, 'dashboard/client.html', context)