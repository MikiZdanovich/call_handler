from data_service.database.models.call_details import CallDetails


def get_saved_data():
    records = CallDetails.query.all()
    return ([u.as_dict() for u in records])
