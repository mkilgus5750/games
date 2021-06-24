from django.db import models

# Create your models here.

class Round(models.Model):
    points = models.IntegerField()

class Player(models.Model):
    name = models.CharField(max_length=80)
    # game_count = self.Game_set.count()

class Game(models.Model):
    name = models.CharField(max_length=80)
    rounds = models.ForeignKey(Round, on_delete=models.SET_NULL, null=True)
    players = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    # total_points = self.rounds.points.count()
