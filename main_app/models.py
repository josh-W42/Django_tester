from django.db import models

# Create your models here.
class Cat(models.Model):
  age = models.IntegerField()
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=300)


  def __str__(self) -> str:
      return self.name