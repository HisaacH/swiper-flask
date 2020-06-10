#!./.venv/bin/python

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from commen import db
from main import app

manager = Manager(app)
migration = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
