from datetime import datetime, timezone
import json
import random
import string
from time import sleep

path = "call_data_lake"


def random_string_digits(stringLength=7):
    """Generate a random of digits """
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(stringLength))


def random_start_call_time():
    return int(datetime.now(tz=timezone.utc).timestamp() * 1000)


def random_end_call_time():
    return random_start_call_time() - int(random_string_digits(2))


def random_band():
    bands = ["GSM", "CDMA", "LTE"]
    return random.choice(bands)


def generate_data( number_of_file=0, sleep_timer=1, ):
    for i in range(number_of_file):
        data = {"number_in": f"{random_string_digits()}",
                "number_out": f"{random_string_digits()}",
                "call_start_time": f"{random_start_call_time()}",
                "call_end_time": f"{random_end_call_time()}",
                "band": f"{random_band()}"}
        serialized = json.dumps(data)
        with open(f"{path}/test_file_{datetime.now().strftime('%f')}.json", 'w+') as file:
            file.write(serialized)
        sleep(sleep_timer)

generate_data(5,1)