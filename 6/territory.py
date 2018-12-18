from collections import defaultdict
import sys


def manh_owner(x: int, y: int, coords: dict) -> int:
    """  returns the closest coordinate for x, y or -1 if there is a tie
    """
    dists = {}
    min_dist = 999
    min_id = -1
    for cid, (cx, cy) in coords.items():
        dist = abs(cx - x) + abs(cy - y)
        dists[cid] = dist
        if x == 0 and y == 50:
            print(cid, x, y, cx, cy, dist)
        if dist < min_dist:
            min_dist = dist
            min_id = cid

    if list(dists.values()).count(min_dist) > 1:
        min_id = -1

    if x == 0 and y == 50:
        print(dists)

    return min_id, min_dist


def execute_input(filename: str) -> int:

    coords = {}
    max_x = max_y = 0
    index = 0
    with open(filename) as f:
        for line in f:
            x = int(line.split(",")[0].strip())
            y = int(line.split(",")[1].strip())
            coords[index] = (x, y)
            index += 1
            if x > max_x:
                max_x = x + 1
            if y > max_y:
                max_y = y + 1

    map = list()
    for _ in range(max_x):
        map.append([(0, 99999)]*max_y)

    for index, xy in coords.items():
        map[xy[0]][xy[1]] = (index, 0)

    map[0][0] = manh_owner(0, 0, coords)

    for x in range(max_x):
        for y in range(max_y):
            map[x][y] = manh_owner(x, y, coords)


    # Fully expanded at this point

    # Remove boundary areas
    boundary = set()
    [boundary.add(i[0]) for i in map[0]]
    [boundary.add(i[0]) for i in map[-1]]
    for line in map:
        boundary.add(line[0][0])
        boundary.add(line[-1][0])

    print("Boundary ids are ", boundary)

    # Count remaining
    counts = defaultdict(lambda: 0)
    for line in map:
        for (id, dist) in line:
            if id not in boundary:
                counts[id] += 1

    print(counts)

    max_area = 0
    max_id = 0
    for id, area in counts.items():
        if area > max_area:
            max_area = area
            max_id = id

    for line in map[34:350]:
        print(''.join(str(x[0]).zfill(2) for x in line[34:130]))

    return max_area, max_id


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_input(sys.argv[1]))
    else:
        print("Please use input file as argument")
