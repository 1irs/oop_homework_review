from dataclasses import dataclass
from math import pi
from typing import Optional
from tabulate import tabulate


@dataclass
class Cylinder:
    # Радиус сечения
    radius: float
    # Высота цилиндра
    height: float

    def check_cylinder_dimensions(self) -> bool:
        # Метод, проверяющий корректно ли задан цилиндр, а именно: радиус > 0, высота > 0.
        return self.radius > 0 and self.height > 0

    def get_cylinder_volume(self) -> Optional[float]:
        # Метод, вычисляющий объем цилиндра.
        if self.check_cylinder_dimensions():
            volume = pi * (self.radius ** 2) * self.height
            return round(volume, 2)


@dataclass
class CylinderDimensions:
    """Хранилище цилиндров"""
    dimensions: list[Cylinder]

    def print_radius_height_volume(self) -> None:
        # Метод, печатающий на экран свойства цилиндра: радиус, высоту, объем.
        #print('Radius | Height | Cylinder Volume')
        rows = []
        for dimension in self.dimensions:
            rows.append([dimension.radius, dimension.height, dimension.get_cylinder_volume()])

        print(tabulate(rows, headers=['Radius', 'Height', 'Cylinder Volume'], tablefmt="grid"))


dimension1 = Cylinder(1, 2)
dimension2 = Cylinder(-1, 2)
dimension3 = Cylinder(1, -2)
dimension4 = Cylinder(3.75, 4.48)
dimension5 = Cylinder(0, 0)
cylinder_dimensions: list[Cylinder] = [dimension1, dimension2, dimension3, dimension4,
                                       dimension5]
cylinder_dimensions1 = CylinderDimensions(cylinder_dimensions)
cylinder_dimensions1.print_radius_height_volume()

