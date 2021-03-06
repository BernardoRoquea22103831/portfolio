# Generated by Django 4.0.4 on 2022-05-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_linguagem_descricao_alter_pessoa_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeAutor', models.CharField(max_length=60)),
                ('titulo', models.CharField(max_length=2000)),
                ('descricao', models.CharField(max_length=2000)),
                ('link', models.CharField(blank=True, max_length=2000)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
