from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

# Create your views here.
def wszystkie_filmy(request):
    # test = 'To jest coś wewnątrz views'
    # return render(request, 'filmy.html', {'filmy' : ['Avatar', 'Titanic']})
    # wszystkie = Film.objects.all()
    wszystkie = []  # wyskoczy na stronie Brak filmów
    return render(request, 'filmy.html', {'filmy': wszystkie})
