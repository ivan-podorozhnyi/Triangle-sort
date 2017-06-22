from abc import ABC, abstractmethod

from core.triangle import Triangles


class TrianglePrinter(ABC):
    @abstractmethod
    def print(self):
        pass


class StdoutTrianglePrinter(TrianglePrinter):
    def __init__(self, triangles: Triangles):
        self._triangles = triangles

    def print(self):
        print("==========Triangles list:==========")

        for i in self._triangles.data:
            print(i)

    @property
    def triangles(self):
        return self._triangles


class SortedTrianglePrinter(TrianglePrinter):
    def __init__(self, triangles: Triangles):
        self._std_printer = StdoutTrianglePrinter(triangles)

    def print(self):
        self._std_printer.triangles.data.sort(key=lambda triangle: triangle.calc_area(), reverse=True)
        self._std_printer.print()
