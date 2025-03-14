from django.db import models
from django.contrib.auth.models import User

class Plainte(models.Model):
    STATUT = [('En attente', 'En attente'),('En cours', 'En cours'),('Résolue', 'Résolue')]
    CATEGORIES = [('Route endommagée', 'Route endommagée'),('Coupure d\'eau', 'Coupure d\'eau'),('Problème d\'électricité', 'Problème d\'électricité'),('autre', 'Autre')]

    citoyen = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=50, choices=CATEGORIES, null=True)
    image=models.ImageField(upload_to='media/', blank=True, null=True)
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT, default='En attente')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.citoyen.username}"