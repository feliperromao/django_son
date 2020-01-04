# Django 

## Cria um novo projeto com django
`$ django-admin startproject nome_do_projeto`

## Inicia o webserver
`$ python manager.py runserver`

## Cria um novo usuario administrador
`$ python manager.py createsuperuser`

## Cria uma nova app no projeto
`$ django-admin strartapp nome_da_app`

# Migrations

## Cria uma nova migrate
`$ python manage.py makemigrations nome_da_app`

## Executa as migrates
`$ python manage.py migrate`

## Ver o sql que será executado no migrate
`$ python manage.py sqlmigrate nome_da_app numero_da_migrate`

## Exibir as migrations
`$ python manage.py showmigrations`


## Executar a aplicação no shell
`$ python manage.py shell`