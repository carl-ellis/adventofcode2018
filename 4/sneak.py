from collections import defaultdict
from datetime import datetime
import sys

"""
Example :
[1518-06-08 23:56] Guard #1559 begins shift
[1518-05-21 00:35] wakes up
[1518-07-07 00:37] falls asleep
"""
FORMATSTR = "%Y-%m-%d %H:%M"

def line_to_dt(line: str) -> datetime:
    return datetime.strptime(line.split("]")[0].split("[")[1], FORMATSTR)

def line_to_data(line: str) -> str:
    return line.split("]")[1]

def data_to_id(data: str) -> int:
    return int(data.split("#")[1].split(" ")[0])

def default_guard_data():
    return [0] * 60

def execute_input(filename: str) -> int:

    records = []

    with open(filename) as f:
        for line in f:
            records.append(line)

    records = sorted(records, key=line_to_dt)

    # Guard data structure
    sneak = defaultdict(default_guard_data)

    current_id = None
    sleeping = False
    for record in records:
        dt = line_to_dt(record)
        data = line_to_data(record)
        if "#" in data:
            current_id = data_to_id(data)
            sleeping = False
        elif current_id and "asleep" in data:
            sleep_minute = dt.minute
            sleep_range = sneak[current_id][sleep_minute:]
            sneak[current_id][sleep_minute:] = list(map(lambda x: x+1, sleep_range))
            sleeping = True
        elif current_id and sleeping and "wakes" in data:
            wake_minute = dt.minute
            wake_range = sneak[current_id][wake_minute:]
            sneak[current_id][wake_minute:] = list(map(lambda x: x-1, wake_range))
            sleeping = False

    highest_id = None
    highest_sleep = 0
    highest_minute = None

    for key, value in sneak.items():
        total_sleep = sum(value)
        if total_sleep > highest_sleep:
            highest_sleep = total_sleep
            highest_id = key
            highest_minute = value.index(max(value))

    print("%s: T%s M%s" % (highest_id, highest_sleep, highest_minute))

    return highest_id * highest_minute


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_input(sys.argv[1]))
    else:
        print("Please use input file as argument")
