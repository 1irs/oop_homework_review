import math
import numpy
from dataclasses import dataclass

@dataclass
class Cylinder:
    """Радиус сечения"""
    sec_radius: float

    """Высота цилиндра"""
    height: float

    """Метод, проверяющий корректно ли задан цилиндр, а именно: радиус > 0, высота > 0."""
    def is_it_cylinder(self) -> bool:
        if self.sec_radius <= 0:
            print(f"This is not a cylinder, because radius is: {self.sec_radius}")
            return False
        if self.height <= 0:
            print(f"This is not a cylinder, because height is: {self.height}")
            return False
        print("This is cylinder")
        return True

    """Метод, вычисляющий объем цилиндра. """
    def volume(self) -> float:
        # return self.height * self.sec_radius * self.sec_radius * 3.14159
        # return self.height * math.pi * pow(self.sec_radius, 2)
        return self.height * numpy.pi * pow(self.sec_radius, 2)

    """Метод, печатающий на экран свойства цилиндра: радиус, высоту, объем."""
    def print_cyl(self):
        if self.is_it_cylinder():
            return print(f"Radius: {self.sec_radius}, height: {self.height}, volume: {self.volume()}")

cyl1 = Cylinder(5, 10)
cyl2 = Cylinder(-1, 10)
cyl3 = Cylinder(10, -5)
cyl4 = Cylinder(-5, 0)
cyl5 = Cylinder(math.pi, numpy.pi)

cyl1.print_cyl()
cyl2.print_cyl()
cyl3.print_cyl()
cyl4.print_cyl()
cyl5.print_cyl()

