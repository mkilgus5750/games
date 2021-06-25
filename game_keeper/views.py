from django.shortcuts import render, get_object_or_404
from .models import Game
# Create your views here.

all_games = Game.objects.all()

def index(request):
    filtered_games = all_games.order_by("-date")[:3]

    return render(request, 'game_keeper/index.html', {
        'games': filtered_games
    })

def games(request):
    games = all_games.order_by("-date")
    return render(request, 'game_keeper/all-games.html', {
        'games': games 
    })

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    all_rounds = game.rounds.all()
    rounds = tuple(round for round in all_rounds),
    players = tuple(round.players.all() for round in all_rounds)
    return render(request, 'game_keeper/game-detail.html', {
        'game': game,
        'rounds': rounds,
        'players': players
    })
    # display round details, winner of each round, winner of each game
    # will have to implement round page and game_detail page