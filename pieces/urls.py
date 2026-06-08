from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.dashboard), name='dashboard'),
    path('pieces/', login_required(views.liste_pieces), name='liste_pieces'),
    path('pieces/ajouter/', login_required(views.ajouter_piece), name='ajouter_piece'),
    path('pieces/<int:pk>/modifier/', login_required(views.modifier_piece), name='modifier_piece'),
    path('pieces/<int:pk>/supprimer/', login_required(views.supprimer_piece), name='supprimer_piece'),
    path('consommation/', login_required(views.consommation), name='consommation'),
    path('reception/', login_required(views.reception), name='reception'),
    path('critiques/', login_required(views.pieces_critiques), name='pieces_critiques'),
    path('historique/', login_required(views.historique), name='historique'),
    path('pieces/export/', login_required(views.export_pieces_excel), name='export_pieces'),
    path('historique/export/', login_required(views.export_historique_excel), name='export_historique'),
    path('utilisateurs/', login_required(views.liste_utilisateurs), name='liste_utilisateurs'),
    path('utilisateurs/ajouter/', login_required(views.ajouter_utilisateur), name='ajouter_utilisateur'),
    path('utilisateurs/<int:pk>/modifier/', login_required(views.modifier_utilisateur), name='modifier_utilisateur'),
    path('utilisateurs/<int:pk>/supprimer/', login_required(views.supprimer_utilisateur), name='supprimer_utilisateur'),
    path('profil/', login_required(views.mon_profil), name='mon_profil'),
    path('critiques/export/', views.export_critiques_excel, name='export_critiques_excel'),

]