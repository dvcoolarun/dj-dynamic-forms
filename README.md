#dj-dynamic-forms

  * if you have to make a dynamic form with Multiple Question of various types?

  * You need dynamic columns in your tables. What do you do?

  * Create lots of tables to handle it. Nice, now you'll need more models and lots of additional sqls. Insertion and selection will be slow as hell.

![](https://aruntakkar.github.io/assets/images/create_form.png)

## How I Solved?
    I use django-hstore package with PostgreSQL to Solve above Problems.
    django-hstore  brings the power of NoSQL key/value stores into PostgreSQL.
    Giving us the advantage of flexibility and performance without loosing the robustness of SQL databases.


## Getting started

    Clone repository
    Virtualenv venv
    source/venv/activate
    pip install -r requirements.txt
    Note:- There is some problem in django-hstore package on pypi right now it will be resolved soon check[https://github.com/djangonauts/django-hstore/issues/154].
    After install django-hstore from pypi using pip install django-hstore[pip install git+https://github.com/djangonauts/django-hstore.git]

## Database Setup
* Create a Database with password,User related to that database in psql shell, For Reference you can pick the existing names or you can change the existing names in settings.py.
* Create a hstore extension for you DB, it is necsarry, Because Most of the DB don't create extension automatically.

## Other Setup
* Social-Authentication is used for user Authentication, So you need to provide oauth authentication token in settings.py after registering you applications.

## Todo
* Rest API For Forms.