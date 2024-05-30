from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
import random

#Incio
def inicio(request):
    return HttpResponse("Hola mica logre hacer una pagina :V")

# #Mostras dia de hoy
# def DiaDeHoy(request):
#         dia = datetime.now() 
#         documentoDeTexto = f"Hoy es dia: <br> {dia}"
#         return HttpResponse(documentoDeTexto)
    
# def miNombreEs(self,nombre):
#      documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
#      return HttpResponse(documentoDeTexto)



def template(request,nombre,apellido,edad):

    fecha = datetime.now()
    return HttpResponse(f"<h1>mi template 1 </h1> ---{fecha} Buenas {nombre} {apellido} edad: {edad} ")


def template2(request,nombre,apellido,edad):
    archivo_abierto = open(r"C:\Users\jigwo\Desktop\Estudios\MiProyecto\plantilla\template2.html")
    # archivo_abierto = open("plantilla\template2.html")
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    fecha = datetime.now()
    datos =  {"fecha": fecha,
              "nombre": nombre,
              "apellido": apellido,
              "edad": edad,
    }
    #crar contexto
    contexto = Context(datos)    
    
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

#sin abrir archivo y cerrar1 
def template3(request,nombre,apellido,edad):
    template = loader.get_template("template2.html")
    
    fecha = datetime.now()
    datos =  {"fecha": fecha,
              "nombre": nombre,
              "apellido": apellido,
              "edad": edad,
    }

    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)

def template4(request,nombre,apellido,edad):
    fecha = datetime.now()
    datos =  {"fecha": fecha,
              "nombre": nombre,
              "apellido": apellido,
              "edad": edad,
    }
    return render(request, "template2.html", datos)


def probando(request):
    
    lista = list(range(500))
    numeros = random.choices(lista, k=50)
    return render(request,"probando.html", {"numeros": numeros})