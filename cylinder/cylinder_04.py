from dataclasses import dataclass
from math import pi


@dataclass
class Cylinder:
    # Радиус сечения
    r: float
    # Высота цилиндра
    l: float

    def check_cylinder_dimensions(self) -> bool:
        # Метод, проверяющий корректно ли задан цилиндр, а именно: радиус > 0, высота > 0.
        return self.r > 0 and self.l > 0

    def get_cylinder_volume(self) -> float:
        # Метод, вычисляющий объем цилиндра.
        if self.check_cylinder_dimensions() is True:
            volume = pi * (self.r ** 2) * self.l
            return round(volume, 2)


@dataclass
class CylinderDimensions:
    dimensions: list[Cylinder]

    def print_radius_height_volume(self) -> None:
        # Метод, печатающий на экран свойства цилиндра: радиус, высоту, объем.
        print('Radius | Height | Cylinder Volume')
        for dimension in self.dimensions:
            print(dimension.r, '|', dimension.l, '|', dimension.get_cylinder_volume())


dimension1 = Cylinder(1, 2)
dimension2 = Cylinder(-1, 2)
dimension3 = Cylinder(1, -2)
dimension4 = Cylinder(3.75, 4.48)
dimension5 = Cylinder(0, 0)
cylinder_dimensions: list[Cylinder] = [dimension1, dimension2, dimension3, dimension4,
                                       dimension5]
cylinder_dimensions1 = CylinderDimensions(cylinder_dimensions)
cylinder_dimensions1.print_radius_height_volume()
