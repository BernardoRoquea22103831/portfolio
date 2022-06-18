#  hello/views.py
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import *
from .models import *


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def layout_page_view(request):
    return render(request, 'portfolio/layout.html')


def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')


def blog_page_view(request):
    context = {
        'blogs': Blog.objects.all
    }
    return render(request, 'portfolio/blog.html', context)


@login_required
def nova_page_view(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {
        'form': form
    }
    return render(request, 'portfolio/nova.html', context)


def novaProjeto_page_view(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projeto'))
    context = {
        'form': form
    }
    return render(request, 'portfolio/novoProjeto.html', context)


def novaLicenciatura_page_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('menu2:cadeira'))
    context = {
        'form': form
    }
    return render(request, 'menu2/novaLicenciatura.html', context)


def projetos_page_view(request):
    context = {
        'projetos': Projeto.objects.all()
    }
    return render(request, 'portfolio/projetos.html', context)


def web_page_view(request):
    return render(request, 'portfolio/web.html')


def layout_page_view(request):
    return render(request, 'portfolio/layout.html')


def about_page_view(request):
    return render(request, 'portfolio/about.html')


def login_page_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'portfolio/login.html', {
                'message': "Invalid credentials."
            })
    return render(request, "portfolio/login.html")


def logout_page_view(request):
    logout(request)
    return render(request, 'portfolio/home.html', {
        "message": "logged out"
    })


def apetidoes_page_view(request):
    return render(request, 'menu2/aptidoes.html')


def certificados_page_view(request):
    return render(request, 'menu2/certificados.html')


def educacao_page_view(request):
    return render(request, 'menu2/educacao.html')


def hobbies_page_view(request):
    return render(request, 'menu2/hobbies.html')


def habilitacoes_page_view(request):
    return render(request, 'menu2/habilitacoes.html')


def licenciatura_page_view(request):
    context = {
        'cadeiras': Cadeira.objects.all(),

    }
    return render(request, 'menu2/licenciatura.html', context)


def editarBlog_page_view(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {
        'form': form, 'blog_id': blog_id
    }
    return render(request, 'portfolio/editarBlog.html', context)
