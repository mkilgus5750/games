from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'game_keeper/index.html')

def game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'game_keeper/includes/game.html', {
        'game': game
    })