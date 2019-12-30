from data_service.database.models import base
from sqlalchemy import Column, Integer, String, ForeignKey


class Tariff(base):
    """ Tariff Model for storing  related details """
    __tablename__ = "Tariff details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    band_type = Column(String(255), nullable=False)
    price = Column(Integer(), unique=False)
