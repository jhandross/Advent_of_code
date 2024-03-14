from collections import namedtuple

input_data = open("16.txt").read()

Room = namedtuple("Room", "rate exits")

def parse_data(lines):
    rooms = {}
    for line in lines:
        line = line.replace(",", "").split()
        source, rate, exits = line[1], int(line[4][5:-1]), line[9:]
        rooms[source] = Room(rate, exits)

    return rooms


def find_distances(rooms):
    key_rooms = {r for r in rooms if rooms[r].rate > 0 or r == "AA"}
    distances = {}

    for start_room in rooms:
        if start_room not in key_rooms: continue
        cur, next, dist = set([
            start_room,
        ]), set(), 0
        distances[(start_room, start_room)] = 0
        while cur:
            dist += 1
            for pos in cur:
                for newpos in rooms[pos].exits:
                    if (start_room, newpos) not in distances:
                        distances[(start_room, newpos)] = dist
                        next.add(newpos)
            cur, next = next, set()

    return distances, key_rooms


def main():
    rooms = parse_data(input_data.split("\n"))
    distances, key_rooms = find_distances(rooms)
    print(len(key_rooms), "important rooms found.")

    def find_best_total_flow(cur="AA", time=30, seen=set(), targets=key_rooms):
        seen = seen | {cur}
        targets = targets - seen

        best_flow = 0
        for target in targets:
            time_left = time - distances[(cur, target)] - 1
            if time_left > 0:
                flow = rooms[target].rate * time_left
                flow += find_best_total_flow(target, time_left, seen, targets)
                if flow > best_flow: best_flow = flow
        return best_flow
    print("Part 1:", find_best_total_flow())

    endpoints = {}
    def find_and_record(cur="AA", curflow=0, time=26, seen=set()):
        seen = seen | {cur}
        targets = key_rooms - seen

        torecord = frozenset(seen - {"AA"})
        if torecord in endpoints:
            endpoints[torecord] = max(endpoints[torecord], curflow)
        else:
            endpoints[torecord] = curflow

        best_flow = 0
        for target in targets:
            time_left = time - distances[(cur, target)] - 1
            if time_left > 0:
                newflow = rooms[target].rate * time_left
                newflow += find_and_record(target, curflow + newflow, time_left, seen)
                if newflow > best_flow: best_flow = newflow
        return best_flow
    find_and_record()

    def fill_in_endpoints(cur=frozenset(key_rooms - {"AA"})):
        if cur not in endpoints:
            best_flow = 0
            for e in cur:
                subset = cur-{e}
                new_flow = fill_in_endpoints(subset)
                if new_flow > best_flow: best_flow = new_flow
            endpoints[cur] = best_flow
        return endpoints[cur]
    fill_in_endpoints()

    best_flow = 0
    for human_work in endpoints:
        elephant_work = frozenset(key_rooms - {"AA"} - human_work)
        total_flow = endpoints[human_work] + endpoints[elephant_work]
        if total_flow > best_flow:
            best_flow = total_flow
    print("Part 2:", best_flow)

if __name__ == "__main__":
    main()
