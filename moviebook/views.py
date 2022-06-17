from django.shortcuts import render
from django.views import generic

from .models import Film

class FilmIndex(generic.ListView):

    template_name = "moviebook/film_index.html"
    context_object_name = "filmy" 

    def get_queryset(self):
        return Film.objects.all().order_by("-id")

class CurrentFilmView(generic.DetailView):

    model = Film
    template_name = "moviebook/film_detail.html"