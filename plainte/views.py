from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login,logout
from django.contrib.auth.forms import AuthenticationForm
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
def inscription(request):
    if request.method == 'POST':
        form = Inscription(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Connecter automatiquement
            return redirect('login')
    else:
        form = Inscription()

    return render(request, 'inscrire.html', {'form': form})

#fonction pour se connecter

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('acceuil')
    else:
        form = AuthenticationForm()
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

