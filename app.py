from core.input import YesInput
from core.printer import SortedTrianglePrinter
from core.triangle import Triangles, triangle_init


def main():
    print("Please input the parameters of triangle:")
    try:
        new_triangle = triangle_init()
    except:
        raise Exception("Value can't be empty and sides must be a number.")
    triangles_list = Triangles(new_triangle)
    answer = YesInput().value()
    while answer == "y" or answer == "yes":
        try:
            triangles_list = triangles_list.with_triangle(triangle_init())
            answer = YesInput().value()
        except:
            raise Exception("Value can't be empty and sides must be a number.")
    SortedTrianglePrinter(triangles_list).print()


if __name__ == '__main__':
    main()
