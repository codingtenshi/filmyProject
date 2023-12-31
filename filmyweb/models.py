from django.db import models

# Create your models here.
class Film(models.Model):
    tytuł = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default='')
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,null=True, blank=True)
    plakat = models.ImageField(upload_to='plakaty', null=True, blank=True)


    def __str__(self):
        return self.tytuł_z_rokiem()
    
    def tytuł_z_rokiem(self):
        return "{} ({})".format(self.tytuł, self.rok)


