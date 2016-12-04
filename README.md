GlassBlower 
===========

##The Best Flask Boilerplate!!

###### GlassBlower is an implementation based on the Rails style

Fist steps:

```
$ virtualenv venv  #in your current directory, to generate de virtual envairoment

$ source venv/bin/activate

$ pip install -r requirements.txt #this file contain Flask-libs

#(optional)start database
$ python manage.py db init 

#(require 4) first migrate
$ python manage.py db migrate 

#(require 5) update database
$ python manage.py db upgrade 

#for run the server, is like django manage.py
$ python manage.py runserver 
```

1. Config database and enviroment work: <br>
config/config.py 
 
2. Add the routes in: <br>
config/routes.py 

## Structure Tree of GlassBlower:

```
glassBlower/

├── app 
│   ├── forms 
│   ├── models 
│   ├── templates 
│   │   └── index.html 
│   └── views 
│       └── index.py 
├── config 
│   ├── config.py 
│   └── routes.py 
├── glassblower.py 
├── manage.py 
├── requirements.txt 
├── static 
│   ├── images 
│   │   └── images.png 
│   ├── javascripts 
│   │   └── bootstrap.min.js 
│   └── stylesheets 
│       └── bootstrap.min.css 
├── test 
└── wsgi.py 
```


## GlassBlower File creator:

###### You can create views, models and login

* *Create view example*:

```
$ python glassblower.py blow view whatever

this command make:
  app/views/whatever.py
  app/templates/whatever.html

and modify: 
  app/views/__init__.py

you need to update route.py for routing
```

* *Create model example*:

```
$ python glassblower blow model whatever

this command make:
app/models/whatever.py
 
and modify:
app/models/__init__.py

you need to do

$ python manage.py db migrate
$ python manage.py db upgrade
```

* *Create login example*:

```
#In GlassBlower is very simple make a login
$ python glassblower blow login

#you need to do

$ python manage.py db migrate
$ python manage.py db upgrade
```


