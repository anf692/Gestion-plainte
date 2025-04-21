from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db import IntegrityError
from .models import*
from .forms import*

# Create your views here.


@login_required
def ajouter_plainte(request):
    image = None  # Initialisation pour éviter l'erreur en cas de requête GET

    if request.method == 'POST':
        form = AjoutPlainte(request.POST, request.FILES)  # Ajouter request.FILES pour gérer les fichiers
        image = request.FILES.get('image')  # Récupération de l'image

        if form.is_valid():
            plainte = form.save(commit=False)
            plainte.citoyen = request.user
            plainte.save()
            return redirect('index')
    else:
        form = AjoutPlainte()

    return render(request, 'ajout_plainte.html', {'form': form, 'image': image})

#fonction pour s'inscrire
# Inscription d'un nouvel utilisateur
def inscription(request):  # Suppression de @login_required
    if request.method == 'POST':
        form = FormulaireConnexion(request.POST)
        if form.is_valid():
            user = form.save()  # Sauvegarde et récupère l'utilisateur
            # login(request, user)  # Connexion automatique après inscription
            return redirect("connexion")
    else:
        form = FormulaireConnexion()
    
    return render(request, 'inscrire.html', {'form': form})

# Connexion d'un utilisateur
def connexion(request):
    if request.method == 'POST':
        form = Connexion(request.POST)
        
        username = request.POST.get('username')  # Utilisation de .get() pour éviter KeyError
        password = request.POST.get('password')  # Vérifier que le champ HTML a bien name="password"

        user = authenticate(request, username=username, password=password)  # Note: ajout de request comme premier paramètre
        if user is not None:
            login(request, user)  
            return redirect("acceuil")
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
    else:
        form = Connexion()  # Crée un formulaire vide pour les requêtes GET

    return render(request, 'connexion.html', {'form': form})


def Acceuil(request):
    return render(request, "acceuil.html")

#fonction pour afficher la listes des plainte
def index(request):
    categorie_recherche = request.GET.get('categorie', '')
    plaintes = Plainte.objects.all()
    
    if categorie_recherche:
        plaintes = plaintes.filter(categorie=categorie_recherche)

    categories = Plainte.objects.values_list('categorie', flat=True).distinct()

    context = {
        'plaintes': plaintes,
        'categories': categories,
    }
    return render(request, 'index.html', context)

#fonction pour afficher la details de chaque plainte
def details(request, id):
    plaintes = Plainte.objects.get(id=id)
    return render(request, 'details.html', {'plaintes': plaintes})

#fonction pour modifier une plainte
def Modifier (request, id):
    plainte= Plainte.objects.get(id=id)
    if request.method == 'POST':
        form = AjoutPlainte(request.POST,request.FILES, instance=plainte)
        if form.is_valid():
            plainte = form.save(commit=False)
            plainte.citoyen = request.user
            plainte.save()
            return redirect('index')
    else:
        form = AjoutPlainte(instance=plainte)
    return render(request, 'ajout_plainte.html', {'form': form, 'plainte':plainte})

def Supprimer(request,id):
    plainte= Plainte.objects.get(id=id)
    plainte.delete()
    return redirect('index')

def Deconnection(request):
    logout(request)
    return redirect("connexion")

