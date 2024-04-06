from django.contrib import admin
from .models import Ape, HealthRecord, Status

admin.site.register(Ape)
admin.site.register(HealthRecord)
admin.site.register(Status)
