# Generated by Django 4.0.4 on 2022-05-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadeira',
            name='linguagem',
            field=models.ManyToManyField(to='portfolio.linguagem'),
        ),
    ]
