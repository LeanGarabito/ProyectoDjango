from django.http import HttpResponse
from datetime import datetime


#Incio
def inicio(request):
    return HttpResponse("Hola mica logre hacer una pagina :V")

#Mostras dia de hoy
def DiaDeHoy(request):
        dia = datetime.now() 
        documentoDeTexto = f"Hoy es dia: <br> {dia}"
        return HttpResponse(documentoDeTexto)
    
def miNombreEs(self,nombre):
     documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
     return HttpResponse(documentoDeTexto)

    