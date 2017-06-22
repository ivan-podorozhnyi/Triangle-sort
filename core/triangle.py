import math

from core.input import InputFloat, InputStr


class Triangle(object):
    def __init__(self, name: str, a: float, b: float, c: float):
        self._name = name
        self._side_a = a
        self._side_b = b
        self._side_c = c

    def __str__(self) -> str:
        return '[Triangle: {n} ]: {a} cm.'.format(n=self._name, a=self.calc_area())

    def calc_area(self) -> float:
        half = (self._side_a + self._side_b + self._side_c) / 2
        return round(math.sqrt(half * (half - self._side_a) * (half - self._side_b)
                               * (half - self._side_c)), 2)


class Triangles(object):
    def __init__(self, *triangles: Triangle):
        self._data = list(triangles)

    def with_triangle(self, triangle: Triangle):
        return Triangles(triangle, *self._data)

    @property
    def data(self):
        return self._data


def check_sides(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif (c >= a + b) or (a >= b + c) or (b >= a + c):
        return False
    else:
        return True


def triangle_init() -> Triangle:
    name = InputStr("Name:").value()
    a = InputFloat("Side a:").value()
    b = InputFloat("Side b:").value()
    c = InputFloat("Side c:").value()
    if check_sides(a, b, c):
        return Triangle(name, a, b, c)
    else:
        raise Exception("Triangle can't be created!")
