from helpers import get_lines
import math

def get_ids(line):
    result = list()
    for tk in line.split(","):
        if tk == "x":
            continue
        result.append(int(tk))
    return result

def solve1(data):
    start_time = int(data[0])
    bus_ids = get_ids(data[1])
    nearest = start_time
    result = 0
    for id in bus_ids:
        dif = id - (start_time % id)
        if dif < nearest:
            result = id * dif
            nearest = dif
    print(f"part1: {result}")

def arrive_after(timestamp, bus_id):
    return bus_id - (timestamp % bus_id)

def arrive_after_matches(timestamp, bus_id, must_match):
    return (timestamp + must_match) % bus_id == 0

def test_schedule(schedule, ts):
    for bus_id, after in schedule[1:]:
        if not arrive_after_matches(ts, bus_id, after):
            return False
    return True


def solve2(data):
    schedule = list()
    for i, tk in enumerate(data[1].split(",")):
        if tk == "x":
            continue
        schedule.append((int(tk), i))
    
    result = 0
    first_bus = 0
    bus_every = schedule[0][0]
    search_first = 2
    results = list()
    timestamp = first_bus
    for search_first in range(2, len(schedule) + 1):
        results = list()
        smaller_schedule = schedule[:search_first]
        while True:
            if test_schedule(smaller_schedule, timestamp):
                results.append(timestamp)
            if len(results) == 2:
                break
            timestamp += bus_every
        first_bus = results[0]
        bus_every = results[1] - results[0]
    print(f"part2: {results[0]}")


test_data = '''
939
1789,37,47,1889
'''

data = test_data.strip().split("\n")
data = list(get_lines("input-13.txt"))
solve2(data)


# schedule = [(41, 0), (37, 35), (971, 41), (17, 58), (13, 59), (23, 64), (29, 70), (487, 72), (19, 91)]
# print(test_schedule(schedule, 1739111518166502))