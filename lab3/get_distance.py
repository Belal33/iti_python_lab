"""
2-Given two points represented as x1, y1, x2, y2, r the (float)return (float) distance
between them considering the following distance equation.
# d=sqrt((x2-x1)^2+(y2-y1)^2)
"""

import math


def get_distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
