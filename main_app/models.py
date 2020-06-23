from django.db import models

# Create your models here.
class Games(models.Model):
  name = models.CharField(max_length=100)
  console = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  release_date = models.IntegerField()

  def __str__(self):
    return self.name