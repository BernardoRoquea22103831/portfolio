# Generated by Django 4.0.4 on 2022-05-25 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_cadeira_linguagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
