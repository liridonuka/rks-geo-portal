from django.contrib import admin
from .models import Layers, LayersCategory
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

admin.site.register(Layers, LeafletGeoAdmin)
admin.site.register(LayersCategory)
