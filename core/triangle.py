import math

triangles_list = []


class Triangle(object):
    _allowed_attrs = ("name", "side_a", "side_b", "side_c", "area")

    def __setattr__(self, name, value):
        if name not in self._allowed_attrs:
            raise AttributeError(
                "Cannot set attribute {!r} on type {}".format(
                    name, self.__class__.__name__))
        if hasattr(self, name):
            raise ValueError('Attribute %s already has a value and so cannot be written to' % name)
        super(Triangle, self).__setattr__(name, value)

    def __init__(self, name, a, b, c, area):
        self.name, self.side_a, self.side_b, self.side_c, self.area = name, a, b, c, area


def check_sides(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif (c >= a + b) or (a >= b + c) or (b >= a + c):
        return False
    else:
        return True


def add_triangle(name, a, b, c):
    if check_sides(a, b, c):
        area = find_triangle_area(a, b, c)
        triangles_list.append(Triangle(name, a, b, c, area))
    else:
        print("Can't create triangle. Sides values are incorrect!")


def find_triangle_area(a, b, c):
    half = (a + b + c) / 2
    return round(math.sqrt(half * (half - a) * (half - b) * (half - c)), 6)
