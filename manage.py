from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
server = Server(host="0.0.0.0", port=9000)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()