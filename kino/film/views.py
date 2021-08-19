from django.http import HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.views import generic

from .models import Film


class IndexView(generic.ListView):
    template_name = 'film/index.html'
    context_object_name = 'name_film'

    def get_queryset(self):
        return Film.objects.order_by('-add_date')[:5]


def vision(request, film_id):
    name = get_object_or_404(Film, pk=film_id)
    return render(request, 'film/vision.html', {'name': name})
