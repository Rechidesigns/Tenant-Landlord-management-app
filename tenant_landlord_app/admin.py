from django.contrib import admin

from .models import Apartment, Tenant


admin.site.register([Apartment, Tenant])