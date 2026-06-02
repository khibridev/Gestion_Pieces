from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Paiement

admin_only = user_passes_test(lambda u: u.is_staff, login_url='/login/')

@login_required
@admin_only
def liste_paiements(request):
    query = request.GET.get('q', '')
    paiements = Paiement.objects.all()
    if query:
        paiements = paiements.filter(
            contrat__numero__icontains=query
        ) | paiements.filter(
            contrat__client__nom__icontains=query
        ) | paiements.filter(
            contrat__client__prenom__icontains=query
        )
    return render(request, 'paiements/liste.html', {'paiements': paiements, 'query': query})

@login_required
@admin_only
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
@admin_only
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
@admin_only
def supprimer_paiement(request, pk):
    paiement = get_object_or_404(Paiement, pk=pk)
    paiement.delete()
    return redirect('liste_paiements')

@login_required
@admin_only
def detail_paiement(request, pk):
    paiement = get_object_or_404(Paiement, pk=pk)
    return render(request, 'paiements/detail.html', {'paiement': paiement})
import openpyxl
from django.http import HttpResponse

@login_required
@admin_only
def export_excel_paiements(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Paiements"

    headers = ['Contrat', 'Client', 'Montant', 'Date', 'Mode', 'Statut']
    ws.append(headers)

    for paiement in Paiement.objects.all():
        ws.append([
            paiement.contrat.numero,
            str(paiement.contrat.client),
            float(paiement.montant),
            paiement.date_paiement.strftime('%d/%m/%Y'),
            paiement.mode,
            paiement.statut,
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="paiements.xlsx"'
    wb.save(response)
    return response