# Sistema Web Interno de Assistência Técnica de Celulares 

Este é um projeto desenvolvido utilizando Django, um framework web em Python, para fornecer controle interno a uma assistência técnica de aparelhos celulares.

Este README fornece uma visão geral das funcionalidades do sistema e instruções para configuração e execução.

O projeto foi concebido como um meio para desenvolver e aprimorar habilidades no desenvolvimento web nas tecnologias utilizadas e principalmente, Django.

# Funcionalidades

1. **CRUD dos Aparelhos**: Recurso para o cadastramento,atualização,exclusão e visualização dos aparelhos que entram na loja.Cada aparelho é cadastrado em detalhes para o devido controle com os seguintes campos:
    - Modelo do Aparelho
    - Nome do Cliente
    - Telefone do Cliente
    - Email do Cliente
    - Data de Saída
    - Status do Produto
    - Preço do Conserto
    - Técnico Responsável
    - Descrição do Problema

2. **CRUD dos Funcionários**: Cadastro,visualização,edição e exclusão de funcionários da loja.(Apenas para usuários administradores)

3. **Controle de Permissões**: O sistema contém o controle automático de permissões,estabelecendo as permissões e realizando as verificações para os usuários normais(funcionários) e para os administradores
do sistema(donos/gerentes).

4. **Sistema de Notificação ao Cliente**: O sistema atualiza o cliente automaticamente através do email fornecido pelo mesmo a cada atualização de status do aparelho.

5. **Estatistícas Para Visualização**: Página dedicada para os usuários com permissão de administradores visualizarem algumas estatísticas básicas da loja:
    - Número Total de Funcionários
    - Número de Funcionários Por Posição(Atendente,Gerente ou Técnico)
    - Faturamento total(do ínicio até o momento da consulta)
    - Número de Reparos Totais Realizados pela Loja
    - Valor da Folha de Pagamento dos Funcionários

6.**Cadastro de Usuários**: Por se tratar de um sistema interno,os usuários devem ser criados através de um usuário administrador no painel do mesmo indicado abaixo na parte de URL's.
    
# Tecnologias Utilizadas

    -Django
    -HTML
    -CSS

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- **Python**
- **Pip** (gerenciador de pacotes do Python)

## Instalação das Dependências do Projeto

Para instalar todas as dependências necessárias para o funcionamento correto do projeto(especificadas no requirements.txt), utilize o comando:

**pip install -r requirements.txt**

## Criando um Super Usuário(Administrador)

Para configurar um administrador no Django,no terminal,utilize o seguinte comando:

**python manage.py createsuperuser**

Após isso siga os passos descritos no terminal para configurar o mesmo.

## Configuração do Banco de Dados 

Para configurar o banco de dados do projeto são necessários dois comandos na seguinte ordem:

**1 - python manage.py makemigrations**

**2 - python manage.py migrate**

## Configuração de variáveis no arquivo app/settings.py 

No arquivo de configurações gerais do projeto (settings.py) devem ser substituídas as seguintes variáveis : 

EMAIL_HOST_USER = email  # O endereço deve ser o endereço de e-mail do remetente

EMAIL_HOST_PASSWORD = senha  # A senha deve ser a senha do e-mail do remetente

** É sempre recomendado criar um arquivo de variáveis de ambiente para colocar dados sensíveis e importar para o settings.py a/as váriaveis.

## Rodando o Servidor Local

Para iniciar o servidor de desenvolvimento do Django em sua máquina utilize o seguinte comando:

**python manage.py runserver**

Após o comando runserver(acima) o servidor de desenvolvimento pode ser acessado através de : http://127.0.0.1:8000/

## URL's

**OBS: Para o acesso das URL's,os passos anteriores descritos devem ser seguidos corretamente.**

**http://127.0.0.1:8000/**
    Página inicial.Formulário para preenchimento do usuário e senha para realizar o login no sistema.
    Após o login bem sucedido o usuário é redirecionado para a URL /list_devices.
    
**http://127.0.0.1:8000/admin**
    Painel do administrador nativo do framework Django.
    Para ter acesso basta realizar o login.
    
**http://127.0.0.1:8000/list_devices**
    URL responsável pela listagem de todos os aparelhos cadastrados na loja através de uma tabela exibindo os detalhes de cada um e os botões para edição e exclusão dos respectivos aparelhos.

**http://127.0.0.1:8000/create_devices/** 
    URL responsável pelo cadastro de um aparelho através de um formulário.

**http://127.0.0.1:8000/list_technicals/**
    URL responsável pela listagem de todos os funcionários cadastrados da mesma forma da listagem de aparelhos.

**http://127.0.0.1:8000/create_technicals/**
    URL responsável pelo cadastro de um funcionário através de um formulário.

**http://127.0.0.1:8000/technicals_statistics/**
    URL responsável pela exibição das estatísticas descritas nas funcionalidades.
