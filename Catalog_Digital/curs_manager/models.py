from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
# Create your models here.

class Elev(models.Model):
    class Meta:
        verbose_name_plural = "Elevi"
        
    nume = models.TextField()
    prenume = models.TextField()
    an = models.IntegerField(default=1, db_index=True)
    telefon = models.IntegerField(null=True, blank=True)
    cnp_student = models.CharField(unique=True, null=True, blank=True, max_length=13,
                                   validators=[MinLengthValidator(13)])
    
    def __str__(self):
        return f"{self.nume} {self.prenume} AN: {self.an}"
    
    
class Adresa(Elev):
    class Meta:
        verbose_name_plural = "Adrese"
        
    
    strada = models.CharField(max_length=33)
    oras = models.CharField(max_length=30)
    judet = models.CharField(max_length=15)
    cod_postal = models.IntegerField()
    
class AdresNoua(models.Model):
    class Meta:
        verbose_name_plural = "Adrese"
        
    elev = models.ForeignKey(Elev, on_delete=models.CASCADE)
    strada = models.CharField(max_length=33)
    oras = models.CharField(max_length=30)
    judet = models.CharField(max_length=15)
    cod_postal = models.IntegerField()
    
    def __str__(self):
        return f"{self.strada} {self.elev}"
    
    
    
class ElevProfile(models.Model):
    class Meta:
        verbose_name_plural = "Elev Profiles"
    elev = models.OneToOneField(Elev, on_delete=models.CASCADE)
    varsta = models.IntegerField()
    
    def __str__(self):
        return f"{self.elev} Varsta: {self.varsta}"
    