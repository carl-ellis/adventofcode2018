from collections import defaultdict
import sys


def execute_input(filename: str) -> int:

    steps = defaultdict(list)
    done = set()
    order = ""

    with open(filename) as f:
        for line in f:
            name = line.split("can")[0].split("step")[1].strip()
            req = line.split("must")[0].split("Step")[1].strip()

            steps[name].append(req)
            steps[req]

    total_steps = len(steps.keys())

    while len(done) != total_steps:

        # Find candidate steps
        candidates = []
        for id, reqs in steps.items():
            if all(req in done for req in reqs):
                if id not in done:
                    candidates.append(id)
        candidates = sorted(candidates)
        print("Candidates: %s" % candidates)

        move = candidates.pop(0)
        order += move
        done.add(move)

    return order


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_input(sys.argv[1]))
    else:
        print("Please use input file as argument")
