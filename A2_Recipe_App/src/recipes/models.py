from django.db import models

# Create your models here.
class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Intermediate', 'Intermediate'),
        ('Hard', 'Hard')
    ]

    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='(in minutes)')
    ingredients = models.CharField(max_length=450)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES, default='Easy', editable=False)

    def __str__(self):
        return str(self.name)