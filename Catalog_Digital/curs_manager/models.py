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