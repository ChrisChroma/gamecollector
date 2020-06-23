from django.shortcuts import render
from .models import Games

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Games.objects.all()
    return render(request, 'games/index.html', { 'games': games })

def games_detail(request, games_id):
    game = Games.objects.get(id=games_id)
    return render(request, 'games/detail.html', { 'game': game })