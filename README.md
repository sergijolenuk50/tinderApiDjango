py --version 
py -m venv .venv 
.venv\Scripts\activate.bat
deactivate

code .
Install 
Django
vscode-icons
.venv\Scripts\activate.bat
py -m pip install Django
py -m pip install -U pip
py
>>>import django
>>>print(django.get_version())
>>>quit()
django-admin startproject tinderApi
cd tinderApi
py manage.py migrate
py manage.py createsuperuser

<!-- admi -->


Ol@com.ua
Qwerty-1

py manage.py startapp users
py manage.py runserver 9178


python manage.py makemigrations
<!-- дає помилку -->
<!-- python manage.py migrate  -->
pip install djangorestframework  
<!-- перевірка пакету -->
pip list  

<!-- Використовуйте команду, щоб перевірити статус ваших міграцій: -->
python manage.py showmigrations 
<!-- видалити базу -->
del db.sqlite3 

pip install django-cors-headers


pip install djangorestframework djangorestframework-simplejwt


git rm -r --cached .

git add .

git commit -m ".gitignore Fixed"



-------App and Templates--------
.venv\Scripts\activate.bat
cd myblog

SuperAdminKrot1-
.venv\Scripts\activate.bat
pip install mysqlclient
pip install mariadb
cd blog
python manage.py migrate

.venv\Scripts\activate.bat
cd blog
python manage.py startapp posts
py manage.py makemigrations
python manage.py migrate
---------Testing ORM----------

py manage.py shell
>>>from posts.models import Post
>>>p=Post()
>>>p
>>>p.title="Пост №1. Краще ви вигулювати собак у парку."
>>>p.save()
>>>Post.objects.all()
>>>exit()
.venv\Scripts\activate.bat
cd blog
py manage.py runserver 9178
Register user

.venv\Scripts\activate.bat
cd blog
py manage.py startapp users