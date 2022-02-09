import time
class Trafficlight:
    __color:str=['Red','Yellow''Green']
    def switching(self):
        if Trafficlight.__color[0] == 'Red' and Trafficlight.__color[1]  == 'Yellow' and Trafficlight.__color[2] == 'Green':
            i = 0
            while i < 3:
                print(Trafficlight. __color[i])
                if i == 0:
                    time. sleep(7)
                elif i == 1:
                    time. sleep(2)
                elif i == 2:
                    time. sleep(4)
                i += 1
        else:
            print('Порядок переключения светофора нарушен!')
trafficlight = Trafficlight()
trafficlight.switching()

