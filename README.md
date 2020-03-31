# Curso Django

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