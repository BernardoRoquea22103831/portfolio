# Generated by Django 4.0.4 on 2022-05-24 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_competencia_linguagem_pessoa_professor_projeto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='cadeira',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='projeto',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.projeto'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='topicos',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
