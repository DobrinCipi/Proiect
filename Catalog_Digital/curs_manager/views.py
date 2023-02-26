from django.shortcuts import render
from django.http import HttpResponse

from .models import Elev
# Create your views here.
def salut(request):
    return HttpResponse("Salut")

def elevi(request):
    # lista_studenti = ["Sudent1", "Student2"] 
    lista_studenti = Elev.objects.all()
    # #studenti_formatat = ", ".join(lista_studenti)
    # # studenti_formatat = "<br />".join(lista_studenti)
    # lista_formatata = [elev.nume for elev in lista_studenti]
    # #lista_formatata = "<br />".join(lista_formatata)
    # output_string =""
    # for elev in lista_studenti:
    #     rand = f"{elev.nume}, {elev.prenume}<br/>"
    #     output_string += rand
    context = {
        "elevi": lista_studenti
    }
    return render(request, "student.html", context)
    return HttpResponse(output_string)


def contact(request):
    lista_elevi = Elev.objects.all()
    if "an" in request.GET:
        try: 
            lista_elevi = lista_elevi.filter(an=request.GET["an"])
        except ValueError:
            lista_elevi = []
            
    if "nume" in request.GET:
        lista_elevi = lista_elevi.filter(nume=request.GET["nume"])
    
    context = {
        "elevi" : lista_elevi
    }
    return render(request, "contact.html", context)


    