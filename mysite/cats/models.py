from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Cat(models.Model):
    nickname = models.CharField(max_length=200,
                            validators=[MinLengthValidator(2, "Cat name should be greater than 2 character")])
    foods = models.CharField(max_length=200)
    weight = models.PositiveIntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

class Breed(models.Model):
    name = models.CharField(max_length=200,
                            validators=[MinLengthValidator(2, "Breed name should be greater than 1 character")])
    
    def __str__(self):
        return self.name


