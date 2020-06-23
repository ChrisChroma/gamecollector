from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Game:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, console, description, release_date):
    self.name = name
    self.console = console
    self.description = description
    self.release_date = release_date

games = [
  Game('Legend of Zelda', 'NES', 'action adventure game', 1986),
  Game('Marios Bros', 'NES', 'ground breaking platformer', 1983),
  Game('World of Warcraft', 'PC', 'largest current western MMORPG', 2004)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', { 'games': games })