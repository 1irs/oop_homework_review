"""Разработать класс геометрической фигуры цилиндр. У класса должно быть два свойства:
1. Радиус сечения.
2. Высота цилиндра.
У класса должно быть три метода:
1. Метод, проверяющий корректно ли задан цилиндр, а именно: радиус > 0, высота > 0.
2. Метод, вычисляющий объем цилиндра.
3. Метод, печатающий на экран свойства цилиндра: радиус, высоту, объем."""

from dataclasses import dataclass, asdict

@dataclass
class Cylinder:
    radius: float
    height: float

    def get_volume(self) -> float:
        """Вычисляет объем цилиндра: как произведение радиуса на высоту"""
        return self.radius * self.height

    def is_correct(self) -> bool:
        """Вычисляет корректно ли задан цилиндр, а именно: радиус > 0, высота > 0"""
        return self.radius, self.height > 0

    def get_size(self) -> str:
        """Метод, печатающий на экран свойства цилиндра: радиус, высоту, объем"""
        return f"Радиус {c1.radius}, {c1.height}"

c1 = Cylinder(radius=50.0, height=10.0)

print(f"Объем цилиндра {c1.get_size()},  {c1.get_volume()}, цилиндр корректно задан: {c1.is_correct()}")



