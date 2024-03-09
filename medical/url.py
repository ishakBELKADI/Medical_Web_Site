
from django.urls import path
from  . import views

urlpatterns = [
 
path('',views.homepage),
path('home/rendezvous',views.rndv),
path('home/rendezvous/prendre',views.Prndv),
path('home/rendezvous/consulter',views.Crndv),
path('home/rendezvous/annuler',views.Arndv),
# path('home/medecin',views.medecin_view),
path('home/Login/medecin/remplirDossierMedical',views.remplirDM),
path('home/Login/medecin/consulterRdvMedecin',views.CrdvMedecin),
path('home/patien/dossiermedical',views.dossierMed_view),
]