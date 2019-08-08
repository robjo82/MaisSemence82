from django.db import models
from django.contrib.auth.models import User


class UserExtention (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    phone_number = models.CharField (max_length = 10, null = True, blank=True)
    postal_code = models.IntegerField (null = True, blank=True)
    town = models.CharField (max_length=50, null=True, blank=True)
    id_card_recto = models.ImageField (upload_to = 'pictures/id_card_recto', null=True, blank=True) 
    id_card_verso = models.ImageField (upload_to = 'pictures/id_card_verso', null=True, blank=True)
    vital_card = models.ImageField (upload_to = 'pictures/vital_card', null=True, blank=True)
    hours_number = models.IntegerField (null=True, blank=True)


    def __str__(self):
        return "Profil de {}".format(self.user.username)