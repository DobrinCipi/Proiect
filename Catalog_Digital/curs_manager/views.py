from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def salut(request):
    return HttpResponse("Salut")

def elevi(request):
    lista_studenti = ["Sudent1", "Student2"] 
    #studenti_formatat = ", ".join(lista_studenti)
    studenti_formatat = "<br />".join(lista_studenti)
    return HttpResponse(studenti_formatat)