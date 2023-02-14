from django.shortcuts import render
from django.http import HttpResponse

from .models import Elev
# Create your views here.
def salut(request):
    return HttpResponse("Salut")

def elevi(request):
    lista_studenti = ["Sudent1", "Student2"] 
    lista_studenti = Elev.objects.all()
    #studenti_formatat = ", ".join(lista_studenti)
    # studenti_formatat = "<br />".join(lista_studenti)
    lista_formatata = [(elev.nume, elev.prenume) for elev in lista_studenti]
    return HttpResponse(lista_formatata)


def contact(request):
    return render(request, "contact.html")
    