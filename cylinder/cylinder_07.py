class Cylinder:

    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def correctness(self):
        if int(self.radius) > 0 and int(self.height) > 0:
            return True
        else:
            return False

    def volume(self):
        volume: float = 0
        pi: float = 3.14
        if self.correctness() is True:
            volume = pi * height * radius * radius
        return volume

    def properties(self):
        print(f" Radius id {radius}, \n Height is {height},\n Volume is {self.volume()}")


if __name__ == '__main__':
    radius: float = 0
    height: float = 0

    radius = float(input("Cylinder Radius is <- "))
    height = float(input("Cylinder Height is <- "))

    s = Cylinder(radius=radius, height=height)
    s.correctness()
    s.volume()
    s.properties()