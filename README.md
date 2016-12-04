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
│   └── routes.blz 
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

###### You can create views, models, api, login and scaffolding

* *Create view example*:

```
$ python glassblower.py blow view --newFile whatever

this command make:
  app/views/whatever.py
  app/templates/whatever.html

and modify: 
  app/views/__init__.py

you need to update route.py for routing
```

* *Create model example*:

```
$ python glassblower.py blow model --newFile whatever

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
In GlassBlower is very simple make a login

$ python glassblower.py blow login

You need to do after:

$ python manage.py db migrate
$ python manage.py db upgrade
```

* *Create api example*:

```
This command make rest api

$ python glassblower.py blow api --newFile whatever


You need to do after modify models file:

$ python manage.py db migrate
$ python manage.py db upgrade
```

* *Create scaffold example*:

```
$ python glassblower.py blow scaffold --newFile whatever

You need to do after modify models file:

$ python manage.py db migrate
$ python manage.py db upgrade
```

