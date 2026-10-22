from django.contrib.auth import logout as logout_django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == "POST":
        nome_completo = request.POST.get('nome-cadastro')
        email = request.POST.get('email-cadastro')
        senha = request.POST.get('senha-cadastro')

        # Verifica se o e-mail já existe na base de dados
        if User.objects.filter(username=email).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return redirect('usuario:cadastro')

        # Cria a conta usando o EMAIL como username
        user = User.objects.create_user(username=email, email=email, password=senha)
        
        # Guarda o primeiro nome e o sobrenome separados
        partes_nome = nome_completo.strip().split(' ', 1)
        user.first_name = partes_nome[0]
        if len(partes_nome) > 1:
            user.last_name = partes_nome[1]
            
        user.save()
        
        messages.success(request, 'Conta criada com sucesso! Faça login.')
        return redirect('usuario:login')

    return render(request, 'cadastro.html')

def login(request):
    if request.method == "POST":
        email_digitado = request.POST.get('email-entrar')
        senha_digitada = request.POST.get('senha-entrar')

        # Faz a autenticação passando o e-mail no lugar do username
        user = authenticate(request, username=email_digitado, password=senha_digitada)
        
        if user is not None:
            auth_login(request, user)
            return redirect('code_analyzer:code_analyzer') # ou a rota que vai para a app principal
        else:
            messages.error(request, 'E-mail ou senha incorretos.')
            return redirect('usuario:login')

    return render(request, 'index.html')
    
def logout(request):
    logout_django(request)
    return redirect('usuario:login')  # Redireciona para a página de login após o logout