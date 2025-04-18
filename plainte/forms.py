from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Plainte  # Si vous avez un modèle Profile avec le champ Telephone

class AjoutPlainte(forms.ModelForm):
    class Meta:
        model = Plainte
        fields = ['Localiter', 'categorie', 'description', 'image']
        widgets = {
            'Localiter': forms.Select(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }


Utilisateur = get_user_model()

class FormulaireConnexion(UserCreationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
    )
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
    )
    
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmation du mot de passe'}),
    )

    class Meta:
        model = Utilisateur 
        fields = ('username', 'password1', 'password2')

class Connexion(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Nom d\'utilisateur'  # Corrigé le placeholder
        }),
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Mot de passe'
        }),
    )