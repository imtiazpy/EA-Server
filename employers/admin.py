from django.contrib import admin

from .models import EmployerProfile, InvitedCandidate

admin.site.register(EmployerProfile)
admin.site.register(InvitedCandidate)
