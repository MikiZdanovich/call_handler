import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import jsonify
from app.service.call_service import get_saved_data
from data_service.data_handle_service.data_monitoring import monitoring
from app import create_app, db


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@app.route("/", methods=["GET"])
def landing_page():
    return jsonify(get_saved_data())


@manager.command
def data_handle():
    monitoring()


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
