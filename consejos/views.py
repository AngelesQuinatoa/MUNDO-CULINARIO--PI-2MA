from django.shortcuts import render, redirect
from .models import Consejo, Receta
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

#Segundo Crud
def addrecetas(request):
    recetas = Receta.objects.all()
    return render(request, 'consejo_recetas.html', {"recetas": recetas})

def create_receta(request):
    receta = Receta(titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
    receta.save()
    return redirect('/consejos/addrecet/')

def borrar_receta(request, receta_id):
    receta = Receta.objects.get(id=receta_id)
    receta.delete()
    return redirect('/consejos/addrecet/')

def editar(request, receta_id):
    receta = Receta.objects.get(pk = receta_id)
    
    if request.method == 'POST':
        receta.titulo = request.POST['titulo']
        receta.descripcion = request.POST['descripcion']
        receta.save()
        return redirect('/consejos/addrecet/')
    return render(request, 'actualizar.html', {"receta": receta})
