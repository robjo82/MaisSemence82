# Generated by Django 2.2.4 on 2019-09-04 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20190903_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextention',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur'),
        ),
    ]
