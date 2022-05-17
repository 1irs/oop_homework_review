from math import pi
from dataclasses import dataclass

@dataclass
class Cylinder:

    radius: float
    height: float

    # Метод, проверяющий корректно ли задан цилиндр, а именно: радиус > 0, высота > 0
    def is_correct(self) -> bool:
        """
        a or b      =
        F    F      F
        F    T      T
        T    F      T
        T    T      T

        not a       =
            T       F
            F       T
        :return:
        """
        return not(self.radius <= 0 or self.height <= 0)

    # Метод, вычисляющий объем цилиндра
    def get_volume(self) -> float:
        #return round(pi * (self.radius ** 2) * self.height, 2)
        return pi * (self.radius ** 2) * self.height

    # Метод, печатающий на экран свойства цилиндра: радиус, высоту, объем
    def print_properties(self):
        print(f'Свойства цилиндра:\nрадиус: {self.radius}, высота: {self.height}, объем: {round(self.get_volume(), 2)}')
