# 1) Почему исключениие в первом варианте работает, а во втором нет?
# 2) Почему в конце принта всегда выводится None?
# дебагер мне не помог в этом :(
import math


class MyCylinder:
    def __init__(self, radius: float, height: float):
        if radius <= 0 or height <= 0:
            raise Exception("Это не цилиндр, введите значения больше 0")
        self.radius = radius
        self.height = height

    # def radius_or_height_correct(self) -> bool:
    #     if self.radius <= 0 or self.height <= 0:
    #         raise Exception("Это не цилиндр, введите значения больше 0")

    def volume_cylinder(self) -> float:
        return math.pi * (self.radius ** 2) * self.height

    def print_result(self) -> str:
        s = f"Радиус цилиндра: {self.radius} \n" \
              f"Высота цилиндра:{self.height} \n" \
              f"Объём цилиндра: {MyCylinder.volume_cylinder(self)}"
        print(s)
        return s


cylinder1 = MyCylinder(radius=9, height=8)
cylinder2 = MyCylinder(radius=3, height=5)
print("Это cylinder1: ", MyCylinder.print_result(cylinder1), "\n")
print("Это cylinder2: ", MyCylinder.print_result(cylinder2), "\n")
