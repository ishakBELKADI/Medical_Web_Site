from django.db import models
from django.utils import timezone

# Create your models here.
class Medecin (models.Model):
    nomM=models.CharField(max_length=50)
    prenomM=models.CharField(max_length=50)

class Infermier (models.Model):
    nomF=models.CharField(max_length=50)
    prenomF=models.CharField(max_length=50)

class Patient(models.Model):
    nss=models.IntegerField(primary_key=True)
    nomP=models.CharField(max_length=50)
    prenomP=models.CharField(max_length=50)
    dateN=models.DateField(default=timezone.now,null=True)
    telP=models.IntegerField()
    adrP=models.CharField(max_length=50)
    
class Rdv(models.Model):
    dateRdv=models.DateField(default=timezone.now,null=True)
    heureRdv=models.TimeField(default=timezone.now().time())
    estchargéMed=models.ForeignKey(Medecin,on_delete=models.CASCADE,null=True)
    estchargéInf=models.ForeignKey(Infermier,on_delete=models.CASCADE,null=True)
    prendre=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    
class DossierMedical(models.Model):
    diagnostic=models.CharField(max_length=100)
    traitement=models.CharField(max_length=100)
    resultat=models.CharField(max_length=100)
    estlier=models.ForeignKey(Medecin,on_delete=models.CASCADE,null=True)
    correspond=models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
