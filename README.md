# FATEC_DES_WEB_3_2023_Avaliacao

Este projeto consiste em uma aplicação web que permite o cadastro da presença de alunos e sua exibição em uma lista, onde é possível visualizar o nome completo do aluno, seu curso, professor e a data com o horário do registro da presença.

## Tecnologias Utilizadas:
- Python
- Django
- HTML
- CSS

## Funcionalidades
- Cadastro de presença com nome completo, curso, professor e data;
- Exibição de todas as presenças cadastradas em uma lista;

## Como executar o projeto

Para executar o projeto, siga os seguintes passos:

1. Clone o repositório:
git clone https://github.com/Klayvert2003/FATEC_DES_WEB_3_2023_Avaliacao.git

2. Crie um ambiente virtual:
python -m venv venv

3. Ative o ambiente virtual:
- Windows:
venv\Scripts\activate

- Linux/Mac:
source venv/bin/activate

4. Instale as dependências:
 pip install -r requirements.txt

5. Execute as migrações:
python manage.py migrate

6. Execute o servidor:
python manage.py runserver

Acesse o endereço http://127.0.0.1:8000/ em seu navegador para utilizar a aplicação.