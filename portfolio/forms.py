from django.forms import ModelForm

from .models import *


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
