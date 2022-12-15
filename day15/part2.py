import re
import itertools
import functools
from multiprocessing import Pool


class Sensor:
    position = None
    nearest = None
    distance = -1
    border_points = None

    def __init__(self, position, nearest):
        self.position = position
        self.nearest = nearest
        self.distance = abs(position[0] - nearest[0]) + abs(position[1] - nearest[1])
        # self.border_points = self.points()

    def distance_to(self, point):
        return abs(self.position[0] - point[0]) + abs(self.position[1] - point[1])

    def covers(self, point):
        return self.distance_to(point) <= self.distance

    def points(self):
        # print("Getting border")
        res = set()
        for y in range(
            self.position[1] - (self.distance), self.position[1] + self.distance
        ):
            if y < 0:
                continue
            if y > 4000000:
                break
            D_min_ys = (self.distance + 1) - abs(y - self.position[1])
            x1 = self.position[0]
            a = (D_min_ys) + x1
            b = (-1 * (D_min_ys)) + x1

            if 0 <= a <= 4000000:
                res.add((a, y))
            if 0 <= b <= 4000000:
                res.add((b, y))

        return res

    def __str__(self):
        return f"sx={self.position[0]}, sy={self.position[1]} --- bx={self.nearest[0]}, by={self.nearest[1]} - db={self.distance}"

    def __repr__(self):
        return str(self)


def find_intersection(combo):
    intersection = functools.reduce(
        lambda x, y: x.intersection(y.points()), combo, combo[0].points()
    )

    if len(intersection) > 0:
        print(intersection)

    return intersection


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        sensors = []

        for line in lines:
            sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))

            sensor = Sensor((sx, sy), (bx, by))
            sensors.append(sensor)

        # print("Finding combinations")

        candidates = [
            s
            for s in sensors
            if (
                -s.distance <= s.position[0] + s.distance <= 4000000
                and -s.distance <= s.position[1] + s.distance <= 4000000
            )
        ]
        print(len(sensors), len(candidates))

        combos = itertools.combinations(candidates, 4)

        with Pool(4) as p:
            p.map(find_intersection, combos)
