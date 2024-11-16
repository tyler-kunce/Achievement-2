from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120)
    #pic
    notes = models.TextField(default="no notes...")

    def __str__(self):
        return str(self.name)