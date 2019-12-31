import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import jsonify
from app import create_app, db
from app.service.call_service import get_saved_data
from data_service.data_handle_service.data_monitoring import monitoring
from test_data_generator import generate_data
from inserts import seed_test_tariff

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@app.route("/", methods=["GET"])
def landing_page():
    return jsonify(get_saved_data())


# start up data monitoring for call_data_lake dir
@manager.command
def data_handle():
    monitoring()


# generate test data json files
@manager.command
def test_data():
    # setup count of test files
    count = 10
    # setup delay between generated files
    delay = 1
    generate_data(count, delay)


# seed tariff table with test data
@manager.command
def seed_db():
    seed_test_tariff()


# run flask app
@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
