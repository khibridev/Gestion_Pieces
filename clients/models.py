
from django.db import models

class Client(models.Model):
    
    TYPE_SOCIETE = [
        ('SARL', 'SARL'),
        ('SAS', 'SAS'),
        ('Auto-entrepreneur', 'Auto-entrepreneur'),
        ('Autre', 'Autre'),
    ]
    
    nom = models.CharField(max_length=100)        
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)         
    telephone = models.CharField(max_length=20)
    cin = models.CharField(max_length=20, unique=True)
    type_societe = models.CharField(max_length=50, choices=TYPE_SOCIETE)
    date_inscription = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.nom} {self.prenom}"  