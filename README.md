# Sistema Web Interno de Assistência Técnica de Celulares 

Projeto desenvolvido com o framework Django para o controle interno de uma assistência técnica de aparelhos celulares.
Foco principal no backend do sistema.

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
2.**CRUD dos Funcionários**: Cadastro,visualização,edição e exclusão de funcionários da loja.(Apenas para usuários administradores)
3.**Controle de Permissões**: O sistema contém o controle automático de permissões,estabelecendo as permissões e realizando as verificações para os usuários normais(funcionários) e para os administradores
do sistema(donos/gerentes).
4.**Sistema de Notificação ao Cliente**: O sistema atualiza o cliente automaticamente através do email fornecido pelo mesmo a cada atualização de status do aparelho.
5.**Estatistícas Para Visualização**: Página dedicada para os usuários com permissão de administradores visualizarem algumas estatísticas básicas da loja:
    - Número Total de Funcionários
    - Número de Funcionários Por Posição(Atendente,Gerente ou Técnico)
    - Faturamento total(do ínicio até o momento da consulta)
    - Número de Reparos Totais Realizados pela Loja
    - Valor da Folha de Pagamento dos Funcionários

# Tecnologias Utilizadas

    -Django
    -HTML
    -CSS

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- **Python**
- **Pip** (gerenciador de pacotes do Python)

## Instalação das Dependências do Projeto

Para instalar todas as dependências necessárias para o funcionamento correto do projeto(especificadas no requirements.txt) utilize o comando:

**pip install -r requirements.txt**

## Configuração do Banco de Dados 

Para configurar o banco de dados do projeto são necessários dois comandos na seguinte ordem:

**1 - python manage.py makemigrations**

**2 - python manage.py migrate**

## Rodando o Servidor Local

Para iniciar o servidor de desenvolvimento do Django em sua máquina utilize o seguinte comando:

**python manage.py runserver**

