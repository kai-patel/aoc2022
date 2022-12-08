import itertools
import sys

if not sys.argv[1]:
    print("Please supply an input file!")

with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    lines = map(lambda x: x.strip("\n"), lines)

    elves = list(
        filter(
            lambda x: x != [""],
            [list(g) for _, g in itertools.groupby(lines, lambda x: len(x))],
        )
    )

    elves = [list(map(int, x)) for x in elves]
    totals = list(map(sum, elves))

    # Part 1
    print(max(totals))

    # Part 2
    print(sum(sorted(totals, reverse=True)[0:3]))
