from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.dashboard_admin, name='dashboard_admin'),
    path('client/', views.dashboard_client, name='dashboard_client'),
]