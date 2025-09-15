from django.contrib import admin
from .models import EmergencyContact, Alert

admin.site.register(EmergencyContact)
admin.site.register(Alert)