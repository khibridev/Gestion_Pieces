from django.db import models
from clients.models import Client 

class Contrat(models.Model):
    
    STATUT_CHOICES = [
        ('actif', 'Actif'),
        ('expire', 'Expiré'),
        ('resilie', 'Résilié'),
        ('en_attente', 'En attente'),
    ]

    PACK_CHOICES = [
        ('standard', 'Standard - 3000 DH'),
        ('premium', 'Premium - 3900 DH'),
        ('premium_plus', 'Premium+ - 4990 DH'),
        ('domiciliation', 'Domiciliation seule - 2000 DH'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    numero = models.CharField(max_length=20, unique=True)
    pack = models.CharField(max_length=50, choices=PACK_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    adresse_domiciliation = models.TextField()

    def __str__(self):
        return f"Contrat {self.numero} - {self.client}"