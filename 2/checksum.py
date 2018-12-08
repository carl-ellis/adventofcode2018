from collections import defaultdict
import sys


def checksum_box(id: str) -> (bool, bool):
    """ Takes a box name, and returns a tuple that is:
        (F, F) is no letter appears 2 or 3 times,
        (T, F) if at least 1 letter appears 2 times,
        (F, T) if at least 1 letter appears 3 times,
        (T, T) if both conditions are true
    """
    counts = defaultdict(lambda: 0)
    for letter in list(id):
        counts[letter] += 1

    return (2 in counts.values(), 3 in counts.values())


def execute_input(filename: str) -> int:
    """
    For each checksum from each id, return the value
    #2s * #3s
    """
    twos = 0
    threes = 0
    with open(filename) as input:
        for id in input:
            checksum_part = checksum_box(id)
            twos += 1 if checksum_part[0] else 0
            threes += 1 if checksum_part[1] else 0

    return twos * threes


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_input(sys.argv[1]))
    else:
        print("Please use input file as argument")
