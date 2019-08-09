from django.db import models
from django.contrib.auth.models import User


class UserExtention (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, verbose_name='utilisateur')
    phone_number = models.CharField (max_length = 10, null = True, blank=True, verbose_name='numéro de téléphone')
    postal_code = models.IntegerField (null = True, blank=True, verbose_name='code postal')
    town = models.CharField (max_length=50, null=True, blank=True, verbose_name='ville')
    address = models.CharField (max_length=500, null=True, blank=True, verbose_name='adresse')
    id_card_recto = models.ImageField (upload_to = 'pictures/id_card_recto', null=True, blank=True, verbose_name="photo du recto de la carte d'identité") 
    id_card_verso = models.ImageField (upload_to = 'pictures/id_card_verso', null=True, blank=True, verbose_name="photo du verso de la carte d'identité")
    vital_card = models.ImageField (upload_to = 'pictures/vital_card', null=True, blank=True, verbose_name="photo de la carte vitale")
    hours_number = models.IntegerField (null=True, blank=True, verbose_name="nombre d'heure effectuée par le salarié")


    def __str__(self):
        return "Profil de {}".format(self.user.username)