from django.contrib import admin
from .models import Cadeira, Professor, Projeto, Linguagem, Pessoa, Hobbie, Blog

# Register your models here.

admin.site.register(Cadeira)
admin.site.register(Professor)
admin.site.register(Projeto)
admin.site.register(Linguagem)
admin.site.register(Pessoa)
admin.site.register(Hobbie)
admin.site.register(Blog)


