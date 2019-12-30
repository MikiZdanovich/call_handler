from watchdog.observers import Observer
import time
from watchdog.events import LoggingEventHandler
import re
import json
import os
from data_service.database.models.tariff import Tariff
from data_service.data_handle_service.call_service import save_new_call
from data_service.database import session

# set_up path to data directory
path_to_call_data = "../../call_data_lake"


class Handler(LoggingEventHandler):

    def on_created(self, event):
        file_path = file_name_from_event(event,path_to_call_data)
        data = data_gathering(file_path)
        price_of_call = price_calculation(data)
        save_new_call(data, price_of_call)
        remove_file(file_path)

    def on_deleted(self, event):
        print(event)

    def on_moved(self, event):
        print(event)


def file_name_from_event(event, path):
    pattern = r"\\\\(.*)'"
    match = re.search(pattern, str(event))
    file_name = path + "/" + match.group(1)
    return file_name


def get_data_from_file(file_name):
    with open(file_name, "r") as file:
        data = json.loads(file.read())
    return data


def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("file already deleted")


def data_gathering(file_path):
    data = get_data_from_file(file_path)
    return data


def price_calculation(data):
    tariff = session.query(Tariff).filter_by(band_type=data['band']).first()
    start = int(data['call_start_time'])
    end = int(data["call_end_time"])
    long = start - end
    price = long * int(tariff.price)
    return price


def monitoring():
    observer = Observer()
    observer.schedule(Handler(), path_to_call_data, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    monitoring()