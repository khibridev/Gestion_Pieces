from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_paiements, name='liste_paiements'),
    path('ajouter/', views.ajouter_paiement, name='ajouter_paiement'),
    path('modifier/<int:pk>/', views.modifier_paiement, name='modifier_paiement'),
    path('supprimer/<int:pk>/', views.supprimer_paiement, name='supprimer_paiement'),
    path('detail/<int:pk>/', views.detail_paiement, name='detail_paiement'),
    path('export/excel/', views.export_excel_paiements, name='export_excel_paiements'),
]