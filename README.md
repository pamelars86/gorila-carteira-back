# gorila-carteira-back

## REQUERIMENTOS
# 1. Instalar pip para Python 3
$sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt install python3-pip
# 2. Usar pip para instalar virtualenv
$sudo pip3 install virtualenv 
# 3. Criar o ambiente gorilaenv
$virtualenv -p python3 gorilaenv

## PASSOS
# O backEnd é o framework Django - python3
# Ativar o env: gorilaenv
$/AppGorila/GorilaDjango$ source gorilaenv/bin/activate
(gorilaenv) $AppGorila/GorilaDjango/carteira$ python ./manage.py runserver 8080

# Criar os migrations
(gorilaenv)AppGorila/GorilaDjango/carteira$ python ./manage.py makemigrations carteiraapp
(gorilaenv)AppGorila/GorilaDjango/carteira$ python ./manage.py migrate

# Rodar o servidor
(gorilaenv)AppGorila/GorilaDjango/carteira$ python ./manage.py runserver 8080

# Criar um usuário de superadministrador
(gorilaenv)AppGorila/GorilaDjango/carteira$ python manage.py createsuperuser
Password: **********
Password (again): *********
Superuser created successfully.

# Entrar no administrador e usar o usurio criado anteriormente
http://localhost:8080/admin/
