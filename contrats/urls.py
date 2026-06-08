from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_contrats, name='liste_contrats'),
    path('ajouter/', views.ajouter_contrat, name='ajouter_contrat'),
    path('modifier/<int:pk>/', views.modifier_contrat, name='modifier_contrat'),
    path('supprimer/<int:pk>/', views.supprimer_contrat, name='supprimer_contrat'),
    path('detail/<int:pk>/', views.detail_contrat, name='detail_contrat'),
    path('imprimer/', views.imprimer_contrats, name='imprimer_contrats'),
    path('imprimer/<int:pk>/', views.imprimer_contrat, name='imprimer_contrat'),
]