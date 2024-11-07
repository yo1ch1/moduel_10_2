import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.num_of_knights = 100

    def run(self):
        days_of_fight = 0
        print(f'{self.name}, на нас напали!')
        while True:
            if self.num_of_knights > 0:
                time.sleep(1)
                self.num_of_knights -= self.power
                days_of_fight += 1
                print(f'{self.name} сражается {days_of_fight}..., осталось {self.num_of_knights} воинов.')
            else:
                print(f'{self.name} одержал победу спустя {days_of_fight} дней(дня)!')
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончены!')


