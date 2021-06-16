from django.contrib import admin
from .models import Detail

admin.site.register(Detail)
admin.site.site_header = 'Vaccinated student of SKITM'