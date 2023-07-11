from django.urls import path
from filmyweb.views import wszystkie_filmy, nowy_film, edytuj_filmy, usuń_film

urlpatterns = [
    path('wszystkie/',wszystkie_filmy, name='wszystkie_filmy'),
    path('nowy/', nowy_film, name='nowy_film'),
    path('edytuj/<int:id>/', edytuj_filmy, name='edytuj_filmy'),
    path('usuń/<int:id>/', usuń_film, name='usuń_film'),
]