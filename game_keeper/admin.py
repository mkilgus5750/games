from django.contrib import admin
from .models import Game, Player, Round
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Game, GameAdmin)
admin.site.register(Player)
admin.site.register(Round)