class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия дорожного полотна понадобится {round(asphalt_mass)} кг асфальта')


r = Road(5000, 20)
r.asphalt_mass()