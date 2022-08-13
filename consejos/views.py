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
    consejo = Consejo.objects.get(id=consejo_id)
    consejo.delete()
    return redirect('/consejos/')
