import string
import sys

def collapse_pass(sequence: str) -> (str, int):
    """ Collapses all possible in each pass"""

    new_sequence = ""
    seq_list = list(sequence)
    lastc = seq_list[0]
    skip = 0
    collapses = 0
    for c in seq_list[1:]:

        if skip > 0:
            skip -= 1
            lastc = c
            continue

        if c.upper() == lastc.upper() and c != lastc:
            skip = 1
            collapses += 1
            lastc = c
            continue

        new_sequence += lastc
        lastc = c

    if skip == 0:
        new_sequence += c

    return new_sequence, collapses


def collapse(sequence: str) -> int:
    original_len = len(sequence)

    changes = 1
    while(changes != 0):
        sequence, changes = collapse_pass(sequence)

    return len(sequence), original_len



def execute_input(filename: str) -> int:

    sequence = ""
    with open(filename) as f:
        for line in f:
            sequence += line

    sequence = sequence.strip()

    new_len, original_len = collapse(sequence)
    print("orig: %s" % new_len)

    selected_cha = None
    min_len = new_len

    for cha in string.ascii_lowercase:
        n_sequence = sequence.replace(cha, "").replace(cha.upper(), "")

        new_len, original_len = collapse(n_sequence)
        print("%s: %s" % (cha, new_len))

        if new_len < min_len:
            selected_cha = cha
            min_len = new_len


    return min_len, selected_cha


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_input(sys.argv[1]))
    else:
        print("Please use input file as argument")
