from django.contrib.gis.db import models

# Create your models here.
class LayersCategory(models.Model):
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Layers(models.Model):
    layers_category = models.ForeignKey(LayersCategory, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(unique=True, max_length=200)
    geom = models.GeometryCollectionField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Layers'
