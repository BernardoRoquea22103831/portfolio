from django.urls import path
from . import views

app_name = 'portfolio'

name = 'home'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('blog', views.blog_page_view, name='blog'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('web', views.web_page_view, name='web'),
    path('layout', views.layout_page_view, name='layout'),
    path('about', views.about_page_view, name='about'),
    path('nova', views.nova_page_view, name='nova'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('aptidoes', views.apetidoes_page_view, name='aptidoes'),
    path('certificados', views.certificados_page_view, name='certificados'),
    path('educacao', views.educacao_page_view, name='educacao'),
    path('habilitacoes', views.habilitacoes_page_view, name='habilitacoes'),
    path('hobbies', views.hobbies_page_view, name='hobbies'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('novaLicenciatura', views.novaLicenciatura_page_view, name='novaLicenciatura'),
    path('editarBlog/<int:blog_id>', views.editarBlog_page_view, name='editarBlog'),
    path('novoProjeto',views.novaProjeto_page_view,name='novoProjeto'),
]
