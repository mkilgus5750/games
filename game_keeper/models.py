from django.db import models
import datetime
# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=80)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}, {self.points}'

class Round(models.Model):
    players = models.ManyToManyField(Player)

    def __str__(self):
        return f"{tuple(player for player in self.players.all())}"
    
class Game(models.Model):
    name = models.CharField(max_length=80)
    rounds = models.ManyToManyField(Round)
    slug = models.SlugField(default="")
    date = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return self.name
