import sys

def execute_input(filename: str) -> int:

    # 1000x1000 list
    fabric = []
    for m in range(1000):
        fabric.append([])
        for n in range(1000):
            fabric[m].append(0)

    with open(filename) as input:
        for entry in input:

            # format
            # #ID @ x,y: wxh
            # id = entry.split('@')[0].split('#')[1].strip()
            x = int(entry.split('@')[1].split(':')[0].split(',')[0].strip())
            y = int(entry.split('@')[1].split(':')[0].split(',')[1].strip())
            w = int(entry.split('@')[1].split(':')[1].split('x')[0].strip())
            h = int(entry.split('@')[1].split(':')[1].split('x')[1].strip())

            #print("%s, %s, %s, %s, %s" % (id, x, y, w, h))
            for i in range(w):
                for j in range(h):
                    fabric[y+j][x+i] += 1

        overlaps = 0
        for i in range(1000):
            for j in range(1000):
                if fabric[i][j] > 1:
                    overlaps += 1
            #print(''.join([str(f) for f in fabric[i]]))

    return overlaps


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_input(sys.argv[1]))
    else:
        print("Please use input file as argument")
