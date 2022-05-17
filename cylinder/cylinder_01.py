from dataclasses import dataclass
import math


@dataclass
class Cylinder:
    """
    Класс моделирует цилиндр
    """
    radius: float
    height: float

    def true_cylinder(self) -> bool:
        if self.radius > 0 and self.height > 0:
            print("Цилиндр имеет право на существование")
        else:
            print("Таких цилиндров не бывает")

    def get_cylinder_volume(self) -> float:
        return math.pi * self.radius ** 2 * self.height

    def get_cylinder_properties(self) -> None:

        print(f"Радиус цилиндра {self.radius} \n "
              f"Высота цилиндра {self.height} \n "
              f"Площадь цилиндра {self.get_cylinder_volume()}")


cylinder_number_1 = Cylinder(radius=5, height=10)
cylinder_number_1.true_cylinder()
cylinder_number_1.get_cylinder_properties()

