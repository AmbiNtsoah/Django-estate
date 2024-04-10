from django.db import models


# Create your models here.
""" Notre table Details en model de Class """
class Details(models.Model):
    title = models.CharField(max_length = 250)
    price = models.IntegerField()
    number_of_bathroom = models.IntegerField()
    address = models.CharField( max_length = 250 )

    def __str__(self):
        return self.title