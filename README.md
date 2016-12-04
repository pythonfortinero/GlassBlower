GlassBlower 
===========

The Best Flask Boilerplate!!

GlassBlower is the implementation of a similar structure to Rails

Fist steps:

'''
$ virtualenv venv  #in your current directory, to generate de virtual envairoment

$ source venv/bin.activate

$ pip install -r requirements.txt #this file contain Flask-libs

#(optional)start database
$ python manage.py db init 

#(require 4) first migrate
$ python manage.py db migrate 

#(require 5) update database
$ python manage.py db upgrade 

#for run the server, is like django manage.py
$ python manage.py runserver 
'''

1. #config database and enviroment work
config/config.py 
 
2. #add the routes in:
config/routes.py 

Structure Tree of GlassBlower:

glassBlower/

├── app <br />
│   ├── forms <br />
│   ├── models <br />
│   ├── restful <br />
│   ├── templates <br />
│   │   ├── about.html <br />
│   │   ├── base.html <br />
│   │   └── index.html <br />
│   └── views <br />
│       ├── about.py <br />
│       └── index.py <br />
├── config <br />
│   ├── config.py <br />
│   └── routes.py <br />
├── glassblower.py <br />
├── manage.py <br />
├── requirements.txt <br />
├── static <br />
│   ├── images <br />
│   │   └── flask.png <br />
│   ├── javascripts <br />
│   │   └── bootstrap.min.js <br />
│   └── stylesheets <br />
│       └── bootstrap.min.css <br />
├── test <br />
└── wsgi.py <br />



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
