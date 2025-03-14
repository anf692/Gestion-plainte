from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login
from django.contrib import messages
from .models import*
from .forms import*

# Create your views here.

#fonction pour ajouter  des plaintes
@login_required
def ajouter_plainte(request):
    if request.method == 'POST':
        form = AjoutPlainte(request.POST)
        if form.is_valid():
            plainte = form.save(commit=False)
            plainte.citoyen = request.user
            plainte.save()
            messages.success(request, 'Votre plainte a été enregistrée.')
            return redirect('index')
    else:
        form = AjoutPlainte()
    return render(request, 'ajout_plainte.html', {'form': form})

#fonction pour s'inscrire
def inscription(request):
    if request.method == 'POST':
        form = Inscription(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Connecter automatiquement
            return redirect('index')
    else:
        form = Inscription()

    return render(request, 'inscrire.html', {'form': form})


#fonction pour afficher la listes des plainte
def index (request):
    plaintes = Plainte.objects.all()
    return render(request, 'index.html', {'plaintes': plaintes})

#fonction pour afficher la details de chaque plainte
def details (request, id):
    plaintes = Plainte.objects.get(id=id)
    return render(request, 'details.html', {'plaintes': plaintes})
