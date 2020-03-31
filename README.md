# Curso Django

### Comandos úteis

#### Criando e ativando ambiente virtual
```shell
python -m venv env
source env/bin/activate
```

#### Criando projeto
```shell
django-admin startproject control_gastos .
```

#### Criando a app
```shell
python manage.py startapp contas
```

#### Setando o banco de dados
```shell
python manage.py migrate
```

#### Executando o projeto
```shell
python manage.py runserver
```

#### Criando super usuário
```shell
python manage.py createsuperuser
```

#### Cria as migrations com as novas alterações
```shell
python manage.py makemigrations
# Depois disso rode o migrate
```




### Processo de criação de nova tabela

```shell
# Depois de escrever o model, faça a migration:
python manage.py makemigrations
# Depois execute as migrations no banco de dados:
python manage.py migrate
# Depois registre o model no arquivo de admin:
#
# from .models import Categoria
# admin.site.register(Categoria)
```