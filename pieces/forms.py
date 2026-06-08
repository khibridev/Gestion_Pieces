from django import forms
from .models import Piece


class PieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = ['description', 'reference', 'emplacement', 'stock_reel',
          'fournisseur', 'stock_minimum', 'stock_maximum', 'type_piece' ,'photo']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la pièce'}),
            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: REF-001'}),
            'emplacement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: B1:1'}),
            'stock_reel': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'fournisseur': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_minimum': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'stock_maximum': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'type_piece': forms.Select(attrs={'class': 'form-select'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ConsommationForm(forms.Form):
    piece = forms.ModelChoiceField(
        queryset=Piece.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Pièce',
        empty_label='-- Sélectionner une pièce --'
    )
    quantite = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        label='Quantité consommée'
    )
    commentaire = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Motif de consommation...'}),
        label='Commentaire'
    )


class ReceptionForm(forms.Form):
    piece = forms.ModelChoiceField(
        queryset=Piece.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Pièce',
        empty_label='-- Sélectionner une pièce --'
    )
    quantite = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        label='Quantité reçue'
    )
    commentaire = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'N° bon de livraison, fournisseur...'}),
        label='Commentaire'
    )
