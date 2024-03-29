from collections import defaultdict

def process(log):
    log.sort()

    sleep_data = defaultdict(lambda: [0]*60)

    sd = None
    asleep = False
    for log_entry in log:
        minute = int(log_entry[15:17])
        entry = log_entry[19:].split()

        if entry[0] == "Guard":
            sd = sleep_data[int(entry[1][1:])]

        elif entry[0] == "falls":
            asleep = minute

        elif entry[0] == "wakes":
            wake = minute
            for m in range(asleep, wake):
                sd[m] += 1

    return sleep_data

def part1(sleep_data):
    guard_id, data = max(sleep_data.items(), key=lambda x: sum(x[1]))

    minute, n_sleep = max(enumerate(data), key=lambda x: x[1])
    return n_sleep, guard_id, minute

def part2(sleep_data):
    return max(
        (n_sleep, guard_id, minute) for (guard_id, data) in sleep_data.items() for (minute, n_sleep) in enumerate(data)
        )

if __name__=="__main__":
    with open("04.txt", 'r') as f:
        log = [x.strip() for x in f]

    sleep_data = process(log)
    for p in [part1, part2]:
        n_sleep, guard_id, minute = p(sleep_data)
        print(guard_id * minute)