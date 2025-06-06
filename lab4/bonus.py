# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

# (x, y, z)
# (a, b, c)
# ( ()    )

import math


class Points(object):
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no: "Points"):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no: "Points"):
        return Points(
            self.y * no.z - self.z * no.y,
            -1 * (self.x * no.z - self.z * no.x),
            self.x * no.y - self.y * no.x,
        )

    def absolute(self):
        return pow((self.x**2 + self.y**2 + self.z**2), 0.5)


if __name__ == "__main__":
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = (
        Points(*points[0]),
        Points(*points[1]),
        Points(*points[2]),
        Points(*points[3]),
    )
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
