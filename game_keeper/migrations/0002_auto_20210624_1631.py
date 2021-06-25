# Generated by Django 3.2.4 on 2021-06-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_keeper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='players',
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(to='game_keeper.Player'),
        ),
    ]