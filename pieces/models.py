from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class TypePiece(models.TextChoices):
    MECANIQUE = 'mecanique', 'Mécanique'
    PNEUMATIQUE = 'pneumatique', 'Pneumatique'
    ELECTRIQUE = 'electrique', 'Électrique'
    AUTRE = 'autre', 'Autre'


class Piece(models.Model):
    description = models.CharField(max_length=200, verbose_name="Description")
    reference = models.CharField(max_length=100, unique=True, verbose_name="Référence")
    emplacement = models.CharField(max_length=100, verbose_name="Emplacement")
    stock_reel = models.PositiveIntegerField(default=0, verbose_name="Stock réel")
    fournisseur = models.CharField(max_length=200, verbose_name="Fournisseur")
    stock_minimum = models.PositiveIntegerField(default=0, verbose_name="Stock minimum")
    stock_maximum = models.PositiveIntegerField(default=100, verbose_name="Stock maximum")
    criticite = models.BooleanField(default=False, verbose_name="Pièce critique")
    type_piece = models.CharField(
        max_length=20,
        choices=TypePiece.choices,
        default=TypePiece.MECANIQUE,
        verbose_name="Type de pièce"
    )
    photo = models.ImageField(upload_to='pieces/', blank=True, null=True, verbose_name="Photo")
    date_creation = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Pièce"
        verbose_name_plural = "Pièces"
        ordering = ['description']

    def __str__(self):
        return f"{self.reference} - {self.description}"

    @property
    def est_critique(self):
        return self.stock_reel <= self.stock_minimum

    @property
    def statut_stock(self):
        if self.stock_reel <= self.stock_minimum:
            return 'critique'
        elif self.stock_reel <= self.stock_minimum * 1.5:
            return 'bas'
        return 'normal'


class MouvementStock(models.Model):
    TYPES = [
        ('consommation', 'Consommation'),
        ('reception', 'Réception'),
    ]
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE, related_name='mouvements')
    type_mouvement = models.CharField(max_length=20, choices=TYPES)
    quantite = models.PositiveIntegerField()
    stock_avant = models.PositiveIntegerField()
    stock_apres = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)
    commentaire = models.TextField(blank=True)
    matricule = models.CharField(max_length=50, blank=True, verbose_name="Matricule technicien")

    class Meta:
        ordering = ['-date']
        verbose_name = "Mouvement de stock"

    def __str__(self):
        return f"{self.type_mouvement} - {self.piece.reference} ({self.quantite})"
    from django.contrib.auth.models import User

class Profile(models.Model):
    ROLES = [
        ('admin', 'Administrateur'),
        ('technicien', 'Technicien'),
        ('lecteur', 'Lecteur'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLES, default='technicien')
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True)
    poste = models.CharField(max_length=100, blank=True, verbose_name="Poste / Fonction")

    def __str__(self):
        return f"{self.user.username} — {self.get_role_display()}"

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_technicien(self):
        return self.role == 'technicien'

    @property
    def is_lecteur(self):
        return self.role == 'lecteur'
