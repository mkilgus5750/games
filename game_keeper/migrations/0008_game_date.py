# Generated by Django 3.2.4 on 2021-06-25 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game_keeper', '0007_game_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
