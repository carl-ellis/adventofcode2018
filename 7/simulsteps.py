from collections import defaultdict
import sys


def execute_input(filename: str) -> int:

    steps = defaultdict(list)
    done = set()
    order = ""
    workers = [(0, None)] * 5

    with open(filename) as f:
        for line in f:
            name = line.split("can")[0].split("step")[1].strip()
            req = line.split("must")[0].split("Step")[1].strip()

            steps[name].append(req)
            steps[req]

    total_steps = len(steps.keys())

    seconds = 0

    while len(done) != total_steps:

        # Running steps
        running = {w[1] for w in workers}

        # Find candidate steps
        candidates = []
        for id, reqs in steps.items():
            if all(req in done for req in reqs):
                if id not in done and id not in running:
                    candidates.append(id)
        candidates = sorted(candidates)
        if candidates:
            print("Candidates: %s" % candidates)

        # find free workers
        for index, (rem, item) in enumerate(workers):
            if rem <= 1:
                if item:
                    order += item
                    done.add(item)
                if candidates:
                    move = candidates.pop(0)
                    workers[index] = (ord(move) - ord("A") + 60, move)
                else:
                    workers[index] = (0, None)

            else:
                workers[index] = (rem - 1, item)

        seconds += 1

    return order, seconds


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(execute_input(sys.argv[1]))
    else:
        print("Please use input file as argument")
