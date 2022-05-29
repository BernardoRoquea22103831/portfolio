# Generated by Django 4.0.4 on 2022-05-24 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_hobbie_cadeira_imagem_cadeira_projeto_projeto_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linguagem',
            name='descricao',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='link',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='professor',
            name='link',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='gitHub',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='participantes',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='youtube',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
