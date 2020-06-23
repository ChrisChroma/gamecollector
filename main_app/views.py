from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Games

# Add the following import
from django.http import HttpResponse

class GameCreate(CreateView):
    model = Games
    fields = '__all__'
    success_url = '/games/'

class GameUpdate(UpdateView):
    model = Games
    fields = ['console', 'description', 'release_date']

class GameDelete(DeleteView):
    model = Games
    success_url = '/games/'


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