from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - Coder")

def segundaVista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)

def saludoConNombre(self, nombre):


      return HttpResponse("<h1> Hola" + nombre+" <h1>")

def probandoHtml(self):

    nom="Nahuel"
    ape="Cittadino"
    diccionario={'nombre':nom, 'apellido':ape}

    #miArchivo=open("C:/Users/wellnahuel/Desktop/Seguirclases/Proyecto1/Plantillas/templates1.html")
    plantilla=loader.get_template("templates1.html") 
    #miArchivo.close()
    #contexto=Context(diccionario)

    documento=plantilla.render(diccionario)

    return HttpResponse(documento)