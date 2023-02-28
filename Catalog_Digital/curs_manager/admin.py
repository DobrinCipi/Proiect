from django.contrib import admin

# Register your models here.
from .models import Elev, AdresNoua

class ElevAdmin(admin.ModelAdmin):
    list_display = ("nume", "prenume", "an")
    list_filter = ("an", )
    search_fields = ("nume", "prenume")
    
class AdresaAdmin(admin.ModelAdmin):
    list_display = ("strada", "oras", "elev")
    list_filter = ("elev"), 
 

admin.site.register(Elev, ElevAdmin)
admin.site.register(AdresNoua, AdresaAdmin )