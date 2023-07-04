from django.contrib import admin
from .models import Film

# Register your models here.
# admin.site.register(Film)

@admin.register(Film) # rejestrujemy film; dekorator
class FilmAdmin(admin.ModelAdmin):
    # fields = ['tytuł', 'opis', 'rok']
    # exclude = ['opis']
    list_display = ['tytuł', 'imdb_rating', "rok"]
    list_filter = ('rok',)
    search_fields = ('tytuł','opis')

