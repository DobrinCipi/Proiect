from django.contrib import admin

# Register your models here.
from .models import Elev

class ElevAdmin(admin.ModelAdmin):
    list_display = ("nume", "prenume", "an")
    list_filter = ("an", )
    search_fields = ("nume", "prenume")
    

admin.site.register(Elev, ElevAdmin)