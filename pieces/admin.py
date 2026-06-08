from django.contrib import admin
from .models import Piece, MouvementStock

@admin.register(Piece)
class PieceAdmin(admin.ModelAdmin):
    list_display = ['reference', 'description', 'emplacement', 'stock_reel', 'stock_minimum', 'type_piece']
    list_filter = ['type_piece']
    search_fields = ['reference', 'description', 'fournisseur']

@admin.register(MouvementStock)
class MouvementAdmin(admin.ModelAdmin):
    list_display = ['piece', 'type_mouvement', 'quantite', 'stock_avant', 'stock_apres', 'date']
    list_filter = ['type_mouvement']
