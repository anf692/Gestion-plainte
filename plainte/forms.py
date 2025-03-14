from django import forms
from .models import  Plainte
from django.contrib.auth.models import User

class AjoutPlainte(forms.ModelForm):
    class Meta:
        model = Plainte
        fields = ['categorie', 'description','image']
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class Inscription(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']