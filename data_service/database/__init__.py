from sqlalchemy import create_engine,engine_from_config
from config import DevelopmentConfig
from sqlalchemy.orm import sessionmaker
import os
from data_service.database.models import base
from data_service.database.models.tariff import Tariff
from data_service.database.models.call_details import CallDetails

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')

engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)

base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
