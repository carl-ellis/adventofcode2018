import sys


def execute_input(filename: str) -> str:
    """
    """
    id_repo = []
    with open(filename) as input:
        for id in input:
            id_repo.append(id.strip())

    candidates = []

    # First pass, ids that differ by 1 letter, with dups removed
    for i in id_repo:
        for j in id_repo:
            if i is not j:
                candidates.append((i, j))

    print("Total Candidates: %s" % len(candidates))

    # Second pass, find which id pairs from first pass only differ by 1,
    # ORDERED
    answer = ""
    for (k, l)  in candidates:
        diffs = 0
        diff_chars = ("", "")
        for index in range(len(k)):
            ki = k[index]
            li = l[index]
            if ki != li:
                diffs += 1
                diff_chars = (ki, index)

        if diffs == 1:
            print(k)
            print(l)
            print(diff_chars)
            diff = "%s%s" % (k[0:diff_chars[1]], k[diff_chars[1]+1:])
            print("%s" % diff)
            answer = diff
            break

    return answer



if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_input(sys.argv[1]))
    else:
        print("Please use input file as argument")
