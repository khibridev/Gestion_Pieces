from django.db import models
from contrats.models import Contrat   # on importe le modèle Contrat

class Paiement(models.Model):

    MODE_CHOICES = [
        ('virement', 'Virement bancaire'),
        ('especes', 'Espèces'),
        ('cheque', 'Chèque'),
    ]

    STATUT_CHOICES = [
        ('paye', 'Payé'),
        ('en_attente', 'En attente'),
        ('impaye', 'Impayé'),
    ]

    # ForeignKey = lien entre Paiement et Contrat
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    
    montant = models.DecimalField(max_digits=10, decimal_places=2)  # ex: 3000.00
    date_paiement = models.DateField()
    mode = models.CharField(max_length=50, choices=MODE_CHOICES)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')

    def __str__(self):
        return f"Paiement {self.montant} DH - {self.contrat}"