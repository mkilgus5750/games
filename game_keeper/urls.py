from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games', views.games, name='games'),
    path('games/<slug:slug>', views.game_detail, name='game-detail')
]