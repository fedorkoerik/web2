from django.shortcuts import render
from django.views import generic

from .models import Film

class FilmIndex(generic.ListView):

    template_name = "moviebook/film_index.html" # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    context_object_name = "filmy" # pod tímto jménem budeme volat list objektů v templatu

# tato funkce nám získává list filmů seřazených od největšího id (9,8,7...)
    def get_queryset(self):
        return Film.objects.all().order_by("-id")

class CurrentFilmView(generic.DetailView):

    model = Film
    template_name = "moviebook/film_detail.html"