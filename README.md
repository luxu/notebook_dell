#Project WebScrapping 
Como instalar:

Tenha certeza de estar instalado o python 3.6+ e o git na sua máquina
###Faça o clone do projeto em local de fácil localização:
````
git clone git@github.com:luxu/notebook_dell.git
````
entre na pasta do projeto:
````
cd notebook_dell
````
crie a virtualenv:
````
python -m virtualenv .venv
````
e acesse-a:
````
.venv\Scripts\activate
````
Instale as bibliotecas do projeto
````
pip install -r requirements.txt
````
Rode as migrações: 
````
python manage.py migrate
````
Por fim, rode o projeto
````
python .\manage.py runserver
````
Acesse o site:
````
http://127.0.0.1:8000/
````
Clique no link para rodar o scripts e baixar os notebooks Dell i7
````
Atualizar Lista de Notebooks
````
Ao finalizar click no link para ver o resultado
````
Voltar para home
````