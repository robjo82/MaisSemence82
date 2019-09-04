from django.db import models
from django.contrib.auth.models import User

PLACES_OF_WORK = [
    ('NEGRE', 'negrepelisse'),
    ('DAVY', 'sous chez davy'),
    ('GENE', 'genebriere'),
]

class PlaceOfWork(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    placeofwork = models.CharField(
        max_length=50,
        choices = PLACES_OF_WORK
        )
