from django.urls import path
from .views import addconsejo, create_consejo

urlpatterns = [
    path('', addconsejo),
    path('new/', create_consejo, name='create_consejo'),
]
