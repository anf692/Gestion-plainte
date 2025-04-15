from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Plainte
from django.db.models import Count

@staff_member_required
def dashboard_admin(request):
    if request.method == "POST":
        plainte_id = request.POST.get("plainte_id")
        new_status = request.POST.get("statut")
        plainte = Plainte.objects.get(id=plainte_id)
        plainte.statut = new_status
        plainte.save()
        return redirect('custom_admin:dashboard') 

    plaintes_par_categorie = Plainte.objects.values('categorie').annotate(total=Count('id'))
    plaintes = Plainte.objects.all().order_by('-date_creation')

    return render(request, 'admin/dashboard.html', {
        'plaintes': plaintes,
        'plaintes_par_categorie': plaintes_par_categorie,
    })


class PlainteAdmin(admin.ModelAdmin):
    list_display = ('citoyen', 'categorie', 'statut', 'date_creation')
    list_filter = ('statut', 'categorie')
    search_fields = ('citoyen__username', 'description')

class CustomAdminSite(admin.AdminSite):
    site_header = "Administration des Plaintes"
    site_title = "Admin Plaintes"
    index_title = "Tableau de Bord"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_view(dashboard_admin), name='index'),
            path('dashboard/', self.admin_view(dashboard_admin), name='dashboard'),  # Nom simplifié
        ]
        return custom_urls + urls

admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(Plainte, PlainteAdmin)
