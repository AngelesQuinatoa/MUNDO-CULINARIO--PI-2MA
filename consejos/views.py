from django.shortcuts import render, redirect
from .models import Consejo
# Create your views here.
def addconsejo(request):
    consejos = Consejo.objects.all()
    return render(request, 'addconsejo.html', {"consejos": consejos})

def create_consejo(request):
    consejo = Consejo(titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
    consejo.save()
    return redirect('/consejos/')

def delete_consejo(request, consejo_id):
    consejo = Consejo.objects.get(pk=consejo_id)
    consejo.delete()
    return redirect('/consejos/')

#Enlaces html.

def paginaprincipal(request):
    return render(request, 'paginaprincipal.html')

def recetasnutricional(request):
    return render(request, 'recetasnutricional.html')

def card(request):
    return render(request, 'card.html')

def recetastra(request):
    return render(request, 'recetastra.html')


def postres(request):
    return render(request, 'postres.html')

def recetasint(request):
    return render(request, 'recetasint.html')

def recetasexpress(request):
    return render(request, 'recetasexpress.html')

def consejos(request):
    return render(request, 'consejos.html')

def addreceta(request):
    return render(request, 'addreceta.html')

def noticias(request):
    return render(request, 'noticias.html')

def inicio(request):
    return render(request, 'inicio.html')

def index(request):
    return render(request, 'index.html')

def iniciar(request):
    return render(request, 'iniciar.html')

def queusar(request):
    return render(request, 'queusar.html')

def saludable(request):
    return render(request, 'saludable.html')

def trucosculinarios(request):
    return render(request, 'trucosculinarios.html')


