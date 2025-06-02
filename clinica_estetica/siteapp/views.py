from django.shortcuts import render, get_object_or_404, redirect
from .models import Servico, Profissional, CarrinhoItem
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages

def home(request):
    servicos = Servico.objects.all()
    profissionais = Profissional.objects.all()
    return render(request, 'home.html', {'servicos': servicos, 'profissionais': profissionais})


def agendar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, user=request.user, servico=servico)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AgendamentoForm(user=request.user, servico=servico)
    return render(request, 'agendar.html', {'form': form, 'servico': servico})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')  # redireciona para a view 'home'
            else:
                form.add_error(None, 'Usuário ou senha inválidos')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'user': request.user})

def logout_usuario(request):
    logout(request)
    return redirect('home')

def cadastrar_usuario(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("login")
        else:
            messages.error(request, "Erro ao cadastrar. Verifique os dados.")
    else:
        form = CadastroUsuarioForm()
    return render(request, "cadastro.html", {"form": form})

def carrinho_view(request):
    itens = CarrinhoItem.objects.filter(cliente=request.user)
    total = sum([item.subtotal() for item in itens])
    return render(request, 'carrinho.html', {'itens': itens, 'total': total})

def servico_detalhe(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    return render(request, 'servico_detalhe.html', {'servico': servico})

def perfil_usuario(request):
    if not request.user.is_authenticated:
        return redirect('login')

    agendamentos = Agendamento.objects.filter(cliente=request.user)

    return render(request, 'perfil.html', {
        'usuario': request.user,
        'agendamentos': agendamentos
    })
