from operator import mod
from django.db import models

# Create your models here.
class Movies(models.Model):
    
    Movie_name=models.CharField(max_length=100)
    Release_date=models.DateField()
    Movie_poster=models.ImageField(upload_to='media/poster')
    Languages=models.CharField(max_length=120)
    Gener=models.CharField(max_length=1000)
    About_movie=models.CharField(max_length=20000)
    Movie_trailor=models.URLField()
    Movie_duaration=models.CharField(max_length=20)

    class Meta:
        db_table='movie_tb'
        


