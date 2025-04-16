from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inscription, name='inscrire'),
    path('connexion/', connexion, name='connexion'),
    path('accounts/logout/', Deconnection, name='logout'),
    path('acceuil/', Acceuil, name='acceuil'),
    path('ajouter_plainte/', ajouter_plainte, name='ajouter_plainte'),
    path("list/", index, name='index'),
    path("details/<int:id>", details, name='details'),
    path("modifier/<int:id>", Modifier, name='modifier'),
    path("supprime/<int:id>", Supprimer, name='supprimer'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
