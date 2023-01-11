from django.contrib import admin
from .models import Drugs, illness, BePartner, Recomendations, Pharmacies, Delivery, Apteks

admin.site.register(Drugs)
admin.site.register(illness)
admin.site.register(BePartner)
admin.site.register(Pharmacies)
admin.site.register(Recomendations)
admin.site.register(Delivery)
admin.site.register(Apteks)
