from data_service.database.models import base
from sqlalchemy import Column, Integer, String, ForeignKey
from app import db


class JsonModel(object):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CallDetails(base, db.Model,JsonModel):
    """ Call_details Model for storing call related details """
    __tablename__ = "Call details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    number_in = Column(Integer(), nullable=False)
    number_out = Column(Integer(), unique=False)
    call_start_time = Column(String(255), nullable=False)
    call_end_time = Column(String(255), nullable=False)
    call_price = Column(Integer(), nullable=True)

    def __repr__(self):
        return f"id={self.id}, number_in={self.number_in}," \
               f"number_out = {self.number_out}," \
               f"call_start_time = {self.call_start_time}," \
               f"call_end_time = {self.call_end_time}" \
               f"call_price = {self.call_price}"
