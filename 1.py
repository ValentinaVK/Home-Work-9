from time import sleep


class TrafficLight:
    colors = ['Красный', 'Желтый', 'Зеленый']

    def switching_color(self):
        i = 0
        while i != 3:
            print(TrafficLight.colors[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(4)
            i += 1


color_ = TrafficLight()
color_.switching_color()
