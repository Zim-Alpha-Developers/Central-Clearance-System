from django.contrib import admin
from .models import IndividualDetails

# Register your models here.

admin.site.register(IndividualDetails)
class IndividualDetailsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip', 'country', 'date_of_birth']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip', 'country', 'date_of_birth']
    list_filter = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip', 'country', 'date_of_birth']
    list_editable = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip', 'country', 'date_of_birth']