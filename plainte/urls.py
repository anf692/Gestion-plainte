from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inscription, name='inscrire'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='connexion.html'), name='login'),
    path('accounts/logout/', Deconnection, name='logout'),
    path("list/", index, name='index'),
    path("details/<int:id>", details, name='details'),
    path('ajouter_plainte/', ajouter_plainte, name='ajouter_plainte'),
    

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
