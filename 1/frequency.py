import operator
import sys


func_dict = {"+": operator.add, "-": operator.sub}


def freq_func(total: int, in_str: str) -> int:
    """ Func for folding input and adding or subbing input"""
    print("%s %s" % (total, in_str))
    func = func_dict[in_str[0]]
    input = int(in_str[1:])
    return func(total, input)


def execute_file(filename: str) -> int:

    freq = 0

    with open(filename) as input_file:
        for line in input_file:
            freq = freq_func(freq, line)

    return freq


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_file(sys.argv[1]))
    else:
        print("Please use input file as argument")

