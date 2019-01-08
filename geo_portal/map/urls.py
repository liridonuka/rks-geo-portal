from django.urls import path
from map import views

app_name = 'map'

urlpatterns = [
    path('',views.MapTemplateView.as_view(), name = 'map'),
    path('layers/', views.layers_dataset, name = 'layers'),
    path('categories/', views.categories_dataset, name = 'categories'),
]
