from django.db import models
from django.contrib.auth.models import User 

class HoursDeclaration (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    hours_number = models.FloatField(
        default=0,
        verbose_name="nombre d'heure effectué par le salarié")
