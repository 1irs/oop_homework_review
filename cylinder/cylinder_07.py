import math


class Cylinder:

    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def correctness(self) -> bool:
        return self.radius > 0 and self.height > 0

    def volume(self) -> float:
        volume: float = 0
        pi: float = math.pi
        if self.correctness():
            volume = pi * height * radius ** 2
        return volume

    def properties(self):
        print(f" Radius id {radius}, \n Height is {height},\n Volume is {self.volume()}")


if __name__ == '__main__':

    radius = float(input("Cylinder Radius is <- "))
    height = float(input("Cylinder Height is <- "))

    s = Cylinder(radius=radius, height=height)
    s.correctness()
    s.volume()
    s.properties()