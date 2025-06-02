from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Agendamento, Profissional
from django.contrib.auth.models import User
from django.utils import timezone

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome de usuário'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'especialidade', 'foto']

class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = Cliente  # <- modelo correto
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AgendamentoForm(forms.ModelForm):
    data_hora = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Agendamento
        fields = ['data_hora', 'profissional']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.servico = kwargs.pop('servico')
        super().__init__(*args, **kwargs)
        self.fields['profissional'].queryset = self.servico.profissionais.all()

    def save(self, commit=True):
        agendamento = super().save(commit=False)
        agendamento.cliente = self.user
        agendamento.servico = self.servico
        if commit:
            agendamento.save()
        return agendamento
