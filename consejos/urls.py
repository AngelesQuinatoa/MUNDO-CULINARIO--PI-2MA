from django.urls import path
from .views import addconsejo, create_consejo, delete_consejo, trucosculinarios
from . import views


urlpatterns = [
    path('', addconsejo),
    path('new/', create_consejo, name='create_consejo'),
    path('delete_consejo/<int:consejo_id>/', delete_consejo, name='delete_consejo'),
    path('paginaprincipal/', views.paginaprincipal, name='paginaprincipal'),
    path('card/', views.card, name='card'),
    path('recetasnutricional/', views.recetasnutricional, name='recetasnutricional'),
    path('postres/', views.postres, name='postres'),
    path('recetasint/', views.recetasint, name='recetasint'),
    path('recetasexpress/', views.recetasexpress, name='recetasexpress'),
    path('recetastra/', views.recetastra, name='recetastra'),
    path('consejos/', views.consejos, name='consejos'),
    path('addreceta/', views.addreceta, name='addreceta'),
    path('noticias/', views.noticias, name='noticias'),
    path('inicio/', views.inicio, name='inicio'),
    path('index/', views.index, name='index'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('queusar/', views.queusar, name='queusar'),
    path('saludable/', views.saludable, name='saludable'),
    path('trucosculinarios/', views.trucosculinarios, name='trucosculinarios')
]
