from django.shortcuts import render
from django.views.generic import (View, TemplateView,ListView)
from django.core.serializers import serialize
from django.http import HttpResponse
from layers import models
# Create your views here.


class MapTemplateView(TemplateView):
    template_name = 'map/index.html'

def layers_dataset(request):
    layers = serialize('geojson', models.Layers.objects.all())
    return HttpResponse(layers)

def categories_dataset(request):
    categories = serialize('geojson', models.LayersCategory.objects.all())
    return HttpResponse(categories)
