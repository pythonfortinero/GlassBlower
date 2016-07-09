from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.via import Via

app = Flask(__name__ , template_folder="app/templates", static_url_path='/app/public')
app.config['VIA_ROUTES_MODULE'] = 'config.routes'
db = SQLAlchemy(app)
from app.models import *
via = Via()
via.init_app(app, routes_name='urls')

#app.config.from_object('config.BaseConfig')
app.config.from_object('config.DevelopmentConfig')
migrate = Migrate(app, db)
manager = Manager(app)
server = Server(host="0.0.0.0", port=9000)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()