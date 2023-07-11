from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def wszystkie_filmy(request):
    # test = 'To jest coś wewnątrz views'
    # return render(request, 'filmy.html', {'filmy' : ['Avatar', 'Titanic']})
    wszystkie = Film.objects.all()
    # wszystkie = []  # wyskoczy na stronie Brak filmów
    return render(request, 'filmy.html', {'filmy': wszystkie})

def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
      
    return render(request, 'film_form.html', {'form': form})

@login_required
def edytuj_filmy(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})

@login_required
def usuń_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(wszystkie_filmy)
    
    return render(request, 'potwierdź.html', {'film': film})



    return render(request, 'film_form.html', {'form': form})

