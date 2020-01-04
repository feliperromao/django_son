# Django 

## Cria um novo projeto com django
`$ django-admin startproject nome_do_projeto`

## Inicia o webserver
`$ python manager.py runserver`

## Executa as migrates
`$ python manage.py migrate`

## Cria um novo usuario administrador
`$ python manager.py createsuperuser`

## Cria uma nova app no projeto
`$ django-admin strartapp nome_da_app`

## Cria uma nova migrate
`$ python manage.py makemigrations nome_da_app`

## Ver o sql que será executado no migrate
`$ python manage.py sqlmigrate nome_da_app numero_da_migrate`

## Executar a aplicação no shell
`$ python manage.py shell`

## Exibir as migrations
`$ python manage.py showmigrations`