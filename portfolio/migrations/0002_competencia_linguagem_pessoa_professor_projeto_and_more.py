# Generated by Django 4.0.4 on 2022-05-24 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProfessor', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('descricao', models.CharField(max_length=500)),
                ('anoDeRealizacao', models.IntegerField(default=0)),
                ('gitHub', models.CharField(max_length=2000)),
                ('youtube', models.CharField(max_length=2000)),
                ('participantes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='cadeira',
            name='professorPraticas',
            field=models.ManyToManyField(related_name='caderias', to='portfolio.professor'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='professorTeoricas',
            field=models.ManyToManyField(to='portfolio.professor'),
        ),
    ]