class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f' {self.name}'

    def stop(self):
        return f'\n {self.name} остановилась.'

    def turn(self, direction):
        return f'\n {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return f'\nВаша скорость выше допустимой! Она составляет {self.speed}'
        else:
            return f'Скорость {self.name} является нормальной'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость выше допустимой! Она составляет {self.speed}'
        else:
            return f'Скорость {self.name} является нормальной'


class PoliceCar(Car):
    pass


town = TownCar('NIVA', 70, 'green', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('BMV', 200, 'black', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('Porsche', 220, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('налево'), work.stop())

police = PoliceCar('Nissan', 150, 'blue', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())
