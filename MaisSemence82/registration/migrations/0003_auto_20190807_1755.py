# Generated by Django 2.2.4 on 2019-08-07 15:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0002_remove_profil_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profil',
            new_name='User',
        ),
    ]