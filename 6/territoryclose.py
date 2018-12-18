import sys


def manh_owner(x: int, y: int, coords: dict) -> int:
    """  returns the closest coordinate for x, y or -1 if there is a tie
    """
    dists = {}
    min_id = False
    for cid, (cx, cy) in coords.items():
        dist = abs(cx - x) + abs(cy - y)
        dists[cid] = dist

    if sum(dists.values()) < 10000:
        min_id = True

    return min_id


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
        map.append([False]*max_y)

    for x in range(max_x):
        for y in range(max_y):
            map[x][y] = manh_owner(x, y, coords)


    # Fully expanded at this point

    # Count remaining
    counts = 0
    for line in map:
        counts += line.count(True)

    print(counts)

    for line in map[34:350]:
        print(''.join(str(x)[0] for x in line[34:226]))

    return counts


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_input(sys.argv[1]))
    else:
        print("Please use input file as argument")
