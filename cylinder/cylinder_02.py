import math


class Cylinder:
    def __init__(self, radius: float, height: float):
        assert height > 0, 'Введите высоту больше нуля'
        assert radius > 0, 'Введите радиус больше нуля'
        self.radius = radius
        self.height = height

    def is_correct_cylinder(self) -> bool:
        return self.height > 0 and self.radius > 0

    def get_objom(self) -> float:
        return math.pi*pow(self.radius, 2)*self.height

    def show_cylinder(self) -> str:
        s = f'Радиус цилиндра {self.radius}, высота {self.height} и объем {self.get_objom()}'
        print(s)
        return s


c=Cylinder(5.0, 10.0)
c.show_cylinder()

c2 = Cylinder(0.0, 0.0)


