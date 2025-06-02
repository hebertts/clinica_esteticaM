from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agendar/<int:pk>/', views.agendar_servico, name='agendar_servico'),
    path('login/', views.login_usuario, name='login'),
    path("cadastro/", views.cadastrar_usuario, name="cadastro"),
    path('carrinho/', views.carrinho_view, name='carrinho'),
    path('servico/<int:servico_id>/', views.servico_detalhe, name='servico_detalhe'),
    path('logout/', views.logout_usuario, name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil'),
]
