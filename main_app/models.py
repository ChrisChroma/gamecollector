from django.db import models
from django.urls import reverse

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