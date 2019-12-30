import uuid
from ..database import session
from ..database.models.call_details import CallDetails


def save_new_call(data, price):
    new_record = CallDetails(
        number_in=data['number_in'],
        number_out=data['number_in'],
        call_start_time=data['call_start_time'],
        call_end_time=data['call_end_time'],
        call_price=price)

    session.add(new_record)
    session.commit()
    return "Call details saved"


def get_all_data():
    records = session.query(CallDetails).all()
    for row in records:
        return row.all()
