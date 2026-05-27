from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Paiement

@login_required
def liste_paiements(request):
    paiements = Paiement.objects.all()
    return render(request, 'paiements/liste.html', {'paiements': paiements})

@login_required
def ajouter_paiement(request):
    from contrats.models import Contrat
    contrats = Contrat.objects.all()
    if request.method == 'POST':
        Paiement.objects.create(
            contrat_id=request.POST['contrat'],
            montant=request.POST['montant'],
            date_paiement=request.POST['date_paiement'],
            mode=request.POST['mode'],
            statut=request.POST['statut'],
        )
        return redirect('liste_paiements')
    return render(request, 'paiements/ajouter.html', {'contrats': contrats})

@login_required
def modifier_paiement(request, pk):
    from contrats.models import Contrat
    paiement = get_object_or_404(Paiement, pk=pk)
    contrats = Contrat.objects.all()
    if request.method == 'POST':
        paiement.contrat_id = request.POST['contrat']
        paiement.montant = request.POST['montant']
        paiement.date_paiement = request.POST['date_paiement']
        paiement.mode = request.POST['mode']
        paiement.statut = request.POST['statut']
        paiement.save()
        return redirect('liste_paiements')
    return render(request, 'paiements/modifier.html', {'paiement': paiement, 'contrats': contrats})

@login_required
def supprimer_paiement(request, pk):
    paiement = get_object_or_404(Paiement, pk=pk)
    paiement.delete()
    return redirect('liste_paiements')

@login_required
def detail_paiement(request, pk):
    paiement = get_object_or_404(Paiement, pk=pk)
    return render(request, 'paiements/detail.html', {'paiement': paiement})