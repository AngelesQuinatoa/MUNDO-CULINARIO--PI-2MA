from django.urls import path
from .views import addconsejo, create_consejo, delete_consejo, addrecetas, borrar_receta, create_receta, editar, registro,  trucosculinarios
from . import views
from django.contrib.auth.views import LoginView


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
    path('noticias/', views.noticias, name='noticias'),
    path('inicio/', views.inicio, name='inicio'),
    path('index/', views.index, name='index'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('queusar/', views.queusar, name='queusar'),
    path('saludable/', views.saludable, name='saludable'),
    path('trucosculinarios/', views.trucosculinarios, name='trucosculinarios'),
    path('addrecet/', views.addrecetas, name='addrecet'),
    path('nuevo/', create_receta, name='create_receta'),
    path('borrar_receta/<int:receta_id>/', borrar_receta, name='borrar_receta'),
    path('editar/<int:receta_id>', editar, name='editar'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path('registro/', registro, name='registro')
]



