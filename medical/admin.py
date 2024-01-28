from django.contrib import admin
from .models import Medecin
from .models import Infermier
from .models import Patient
from .models import Rdv
from .models import DossierMedical



# Register your models here.
admin.site.register(Medecin)
admin.site.register(Infermier)
admin.site.register(Patient)
admin.site.register(Rdv)
admin.site.register(DossierMedical)