# Code-Desk 💻📊

**Code-Desk** é uma plataforma web desenvolvida em **Django** para automatizar a análise de código, a correção de exercícios de programação e o acompanhamento do desempenho acadêmico.

A ferramenta permite o upload de pacotes de provas em lote (`.zip`, `.tgz`, `.tar.gz`), organiza automaticamente os arquivos por **turmas** e **estudantes**, exibe o código do aluno lado a lado com o gabarito oficial com destaque de sintaxe, e possibilita o lançamento de notas e justificativas com atualização em tempo real e geração de relatórios consolidados.

---

## ✨ Funcionalidades e destaques

- 🔐 **Autenticação com e-mail:** fluxo de login e cadastro ajustado para usar o e-mail como `username` único no Django, evitando conflitos entre cadastros com nomes iguais.
- 📦 **Suporte a pacotes comprimidos (`.zip`, `.tgz`, `.tar.gz`):** processamento em memória com validações de segurança para arquivos compactados e descompactados.
- 🧩 **Reconhecimento automático de gabaritos:** leitura da pasta `gabarito/` dentro do pacote enviado para pareamento automático das soluções com as submissões dos alunos.
- 🏫 **Agrupamento por turmas e estudantes:** organização hierárquica em árvore no painel lateral (`Turma → Aluno → Questão/Tentativa`).
- ↔️ **Navegação inteligente entre alunos:** botões **Anterior** e **Próximo** para alternar entre as respostas de diferentes estudantes da mesma questão.
- ⚡ **Avaliação em tempo real (Fetch API):** atribuição de nota manual de **0 a 10** e justificativa pedagógica com salvamento assíncrono.
- 📋 **Relatório consolidado de notas (`/Code-Analyzer/relatorio/`):**
  - página dedicada para visualização de relatórios por turma;
  - busca em tempo real por nome ou matrícula;
  - exportação para **PDF** e impressão formatada com `@media print`.
- 🌙 **Tema escuro/claro sincronizado:** alternância dinâmica persistida em `localStorage` com script executado no `<head>` para evitar cintilação ao navegar ou abrir o relatório.

---

## 🛠️ Stack tecnológica

| Camada | Tecnologia |
|---|---|
| **Backend** | Python 3.10+ · Django 6.0+ |
| **Banco de Dados** | SQLite (`db.sqlite3`) |
| **Frontend** | HTML5 · CSS3 · JavaScript ES6+ |
| **Estilização & Ícones** | Bootstrap 5.3.3 · Font Awesome 6.7.2 |
| **Highlighting de código** | Highlight.js 11.9.0 |
| **Autenticação** | `django.contrib.auth` (e-mail como `username`) |

---

## 📁 Estrutura do repositório

```text
Code-Desk/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── LICENSE
├── media/
├── mysite/                       # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│   └── asgi.py
├── code_analyzer/               # Aplicação principal de correção e análise
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       ├── code_analyzer.html
│       └── relatorio.html
├── usuario/                     # Aplicação de autenticação (login, cadastro, logout)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       ├── index.html
│       └── cadastro.html
├── staticfiles/                 # Arquivos estáticos e assets do projeto
│   ├── css/
│   ├── img/
│   └── js/
├── Arquivos de teste/           # Scripts auxiliares para geração de pacotes de teste
│   ├── gerar_test.py
│   └── provas_alunos/
└── README.md
```

---

## ✅ Pré-requisitos

- [Python 3.10 ou superior](https://www.python.org/downloads/)
- `pip` (normalmente incluso com a instalação do Python)
- Git para clonar o repositório

---

## 🚀 Como rodar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/joao-Devr/Code-Desk.git
cd Code-Desk
```

### 2. Criar e ativar um ambiente virtual

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Aplicar as migrações do banco de dados

```bash
python manage.py migrate
```

### 5. Criar um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 6. Rodar o servidor de desenvolvimento

```bash
python manage.py runserver
```

O projeto ficará disponível em:

```text
http://127.0.0.1:8000/
```

Rotas principais:

- `/` — página de login (`usuario`)
- `/cadastro/` — cadastro de novo professor
- `/Code-Analyzer/` — painel principal de correção
- `/Code-Analyzer/relatorio/` — relatório consolidado
- `/admin/` — administração do Django

---

## 📦 Formato esperado do arquivo de submissões

Cada arquivo deve seguir o padrão `a<id_curto>q<questão>t<tentativa>.<extensão>`, por exemplo `a4020q02t01.py`, e conter um cabeçalho em comentário no topo com os metadados do aluno e da submissão:

```text
# Aluno: Nome do Estudante 20221234 (4735)
# Prova: Prova 3 - Quinta 15 (2669)
# Questao: 2, 1a tentativa, nota: 3
# Problema: Matrizes – Matriz Resultante de espaços vazios (1884)
# Turma(s): FP1 3A, semestre: 2026/1, e-mail: nome@dominio.edu
# Justificativa da nota: A quantidade de dados escritos pelo programa é diferente da quantidade de dados esperados.

<código do aluno>
```

Extensões suportadas: `.c`, `.h`, `.cpp`, `.hpp`, `.py`, `.java`, `.js`, `.ts`, `.txt`.

---

## 📄 Licença

Este projeto está licenciado sob os termos da licença [MIT](LICENSE).

---

## 👤 Autor

Desenvolvido por **João Pedro Campolina Rodrigues** ([@joao-Devr](https://github.com/joao-Devr)).
