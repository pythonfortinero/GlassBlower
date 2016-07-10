GlassBlower is the implementation of a similar structure to Rails

Fist steps:

1 $ virtualenv venv  #in your current directory, to generate de virtual envairoment

2 $ source venv/bin.activate

3 $ pip install -r requirements.txt #this file contain Flask-libs

4 $ python manage.py db init #(optional)start database

5 $ python manage.py db migrate #(require 4) first migrate

6 $ python manage.py db upgrade #(require 5) update database

7 $ python manage.py runserver #for run the server, is like django manage.py

8 config/config.py #config database and enviroment work
 
9 config/routes.py #in this file add the routes

Structure Tree of GlassBlower:

glassBlower/

├── app \n
│   ├── forms
│   ├── models
│   ├── restful
│   ├── templates
│   │   ├── about.html
│   │   ├── base.html
│   │   └── index.html
│   └── views
│       ├── about.py
│       └── index.py
├── config
│   ├── config.py
│   └── routes.py
├── glassblower.py
├── manage.py
├── requirements.txt
├── static
│   ├── images
│   │   └── flask.png
│   ├── javascripts
│   │   └── bootstrap.min.js
│   └── stylesheets
│       └── bootstrap.min.css
├── test
└── wsgi.py



GlassBlower File creator:

You can create views and models

Create view example:

$ python glassblower.py blow view whatever

 this command make:
  app/views/whatever.py
  app/templates/whatever.html

 and modify: 
  app/views/__init__.py

 you need to update route.py for routing

Create model example:

$ python glassblower blow model whatever

 this command make:
  app/models/whatever.py
 
 and modify:
  app/models/__init__.py

 you need to do

 $ python manage.py db migrate
 $ python manage.py db upgrade
