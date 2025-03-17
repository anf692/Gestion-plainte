from django import forms
from .models import  Plainte
from django.contrib.auth.models import User

class AjoutPlainte(forms.ModelForm):
    class Meta:
        model = Plainte
        fields = ['Localiter','categorie', 'description','image']
        widgets = {
             'Localiter': forms.Select(attrs={'class': 'form-control'}),
             'categorie': forms.Select(attrs={'class': 'form-control'}),
             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
             'image': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            )
         }

class Inscription(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********'}), label="Mot de passe")
    Telephone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '77 000 00 00'}), label="Telephone")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Example@'}), label="Adress email")
    username = forms.CharField(max_length=150,required=True,label="Nom complet",
        widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}),
        help_text=''  # Supprime le message d'aide
    )

    class Meta:
        model = User
        fields = ['username', 'email','Telephone', 'password']