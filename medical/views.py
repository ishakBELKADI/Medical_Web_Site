from django.http import HttpResponse
from django.shortcuts import render
from .models import DossierMedical, Medecin, Patient,Rdv
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request):
   return render(request,'homr.html')

    
def rndv(request):
   return render(request,'rdv.html')


def Prndv(request):
   if request.method =='POST':
      nss= request.POST['nss']
      nom= request.POST['Nom']
      nomMed=request.POST['doctor']
      prenom=request.POST['Prenom']
      daten=request.POST['DateN']
      tel=request.POST['Tel']
      Adr=request.POST['Adr']
      DateRDV=request.POST['DateRDV']
      heure=request.POST['heure']
      med=Medecin.objects.filter(nomM=nomMed)
      objrdv=Rdv.objects.filter(dateRdv=DateRDV , heureRdv=heure , estchargéMed=med.first())
      if objrdv.exists():
         return HttpResponse("Rdv deja pris veulliez choisir un autre")
    
      obj= Patient.objects.filter(nss=nss)
      
      if(obj.exists()==False):
        patient=Patient.objects.create(
         nss= nss,
         nomP=nom,
         prenomP=prenom,
         dateN=daten,
         telP=tel,
         adrP=Adr)
        rdv= Rdv.objects.create(
         dateRdv=DateRDV,
         heureRdv=heure,
         prendre=patient,
         estchargéMed= med.first()
       )
      else:
         rdv= Rdv.objects.create(
         dateRdv=DateRDV,
         heureRdv=heure,
         prendre=obj.first(),    
         estchargéMed= med.first()

         )
         
      rdvvv=Rdv.objects.get(dateRdv=DateRDV, heureRdv=heure , estchargéMed=med.first())
      p=Patient.objects.get(nss=nss)
      return render(request,'schema.html',{'rdvvv':rdvvv, 'patient':p})
      

   return render(request,'prdv.html')



def Crndv(request):
   ok=1
   if request.method == 'POST':
      print('on est la')
      ok=0
      nss=request.POST['nss']
      query=Patient.objects.filter(nss=nss)
      if query.exists():
         nonInscris=0
         patient=query.first()
         rdvs=Rdv.objects.filter(prendre=patient)
         if rdvs.exists():
           return render(request,'consulterRdv.html',{'rdvs':rdvs, 'patient':patient , 'ok' : ok,'nonInscris':nonInscris})
      else:
         nonInscris=1
         return render(request,'consulterRdv.html',{'ok':ok , 'nonInscris':nonInscris})
           
   return render(request,'consulterRdv.html',{'ok':ok})


def medecin_view(request):
   return render(request,'medcin.html')


def remplirDM(request):
   if request.method == 'POST':
      nomMed=request.POST['nomMed']
      prenomMed=request.POST['prenomMed']
      nomP=request.POST['Nom']
      prenomP=request.POST['Prenom']
      diagnostic=request.POST['diagnostic']
      traitement=request.POST['traitement']
      resultat=request.POST['resultat']
      objpatient=Patient.objects.filter(nomP=nomP , prenomP=prenomP)
      if objpatient.exists()==False :
         return HttpResponse("le patient n'existe pas")
      objmedecin=Medecin.objects.filter(nomM=nomMed , prenomM=prenomMed)
      if objmedecin.exists()==False :
         return HttpResponse("votre nom et prenom erroné! medecin n'existe pas")
      dossier = DossierMedical.objects.create(
         diagnostic=diagnostic,
         traitement=traitement,
         resultat=resultat,
         estlier=objmedecin.first(),
         correspond=objpatient.first()
          )
      print(dossier.estlier.nomM)
      return render(request,'schemaDM.html',{'dossier':dossier})
   return render(request,'RemplirDM.html')

def CrdvMedecin(request):
   ok=1 
   f=0
   if request.method=='POST':
      ok=0
      nomMed=request.POST["nom"]
      prenomMed=request.POST["prenom"]
      querymed=Medecin.objects.filter(nomM=nomMed , prenomM=prenomMed)
      if querymed.exists()==False:
         return HttpResponse("votre nom ou prenom est erroné! medcin n'existe pas")
      med=querymed.first()
      rdvs= Rdv.objects.filter(estchargéMed=med)
      if rdvs.exists()==False:
         f=1
      return render(request,'rdvMedecin.html',{'rdvs':rdvs , 'f':f , 'ok':ok})
      
   return render(request,'rdvMedecin.html',{'ok':ok})
      
      
   
      
  


      

