from django.db import models
from django.urls import reverse

RATING = (
  ('E', 'Everyone'),
  ('T', 'Teen'),
  ('M', 'Mature')
)

# Create your models here.
class Games(models.Model):
  name = models.CharField(max_length=100)
  console = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  release_date = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'games_id': self.id})

class Reviews(models.Model):
  rating = models.CharField(
    max_length=1,
    choices=RATING,
    default=RATING[0][0]
  )

  game = models.ForeignKey(Games, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"Game is rated {self.rating}"