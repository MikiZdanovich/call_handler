from data_service.database.models.call_details import CallDetails


def rep_all_data():
    records = CallDetails.query.all()
    return ([u.as_dict() for u in records])
