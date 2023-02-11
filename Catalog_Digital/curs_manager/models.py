from django.db import models

# Create your models here.

class Elev(models.Model):
    class Meta:
        verbose_name_plural = "Elevi"
        
    nume = models.TextField()
    prenume = models.TextField()
    an = models.IntegerField()
    telefon = models.IntegerField()