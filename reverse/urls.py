from django.urls import include, path
from reverse import views

urlpatterns = [
    path("", views.dna_views)
]
