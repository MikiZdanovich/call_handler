# call_handler
simple app that allow to handle call data file from dir and store it to db, plus simple flask api to fetch saved data
#pre-build folder for incomeing call data file  - call_data_lake

# Migrations:
-python manage.py db migrate
-python manage.py db upgrade

# To seed db with test Tariff data:
-python manage.py seed_db

# To start monitoring of incomeing data files  run - python manage.py data_handle, or python "data_service/data_handle_service/data_monitoring.py"

# To start generating test call data:
-python manage.py test_data, or test_data_generator.py

# To run flask app 
-python manage.py run

# docker and docker-compose do not set-up propertly 
