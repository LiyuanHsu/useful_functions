

from datetime import datetime


def print_time_to_miliseconds():
    print(datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f'))


