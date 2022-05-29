from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Competencia(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=60)
    link = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.nome


class Linguagem(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nomeProfessor = models.CharField(max_length=60)
    link = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.nomeProfessor


class Projeto(models.Model):
    titulo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=500, blank=True)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)
    anoDeRealizacao = models.IntegerField(default=0)
    participantes = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True)
    gitHub = models.CharField(max_length=2000, blank=True)
    youtube = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.titulo


class Cadeira(models.Model):
    nome = models.CharField(max_length=60)
    ano = models.IntegerField(default=0)
    semestre = models.IntegerField(default=0)
    etcs = models.IntegerField(default=0)
    anoLetivo = models.IntegerField(default=0)
    topicos = models.CharField(max_length=100, blank=True)
    rank = models.IntegerField(default=0)
    professorPraticas = models.ManyToManyField(Professor, related_name='cadeiras')
    professorTeoricas = models.ManyToManyField(Professor)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, blank=True, default=None)
    linguagem = models.ManyToManyField(Linguagem, related_name='linguagens')

    def __str__(self):
        return self.nome


class Hobbie(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Blog(models.Model):
    nomeAutor = models.CharField(max_length=60)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=2000)
    descricao = models.CharField(max_length=2000)

    def __str__(self):
        return self.nomeAutor
