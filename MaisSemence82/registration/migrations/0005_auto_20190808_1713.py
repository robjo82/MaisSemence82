# Generated by Django 2.2.4 on 2019-08-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20190807_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextention',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
