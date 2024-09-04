import threading
import time
import random

class BarberShop:
    def __init__(self, num_chairs):
        self.num_chairs = num_chairs  # Инициализация количества стульев
        self.lock = threading.Lock()  # Создание мьютекса для синхронизации потоков
        self.barber_sleeping = True  # Переменная, указывающая, спит ли парикмахер
        self.client_waiting = False  # Переменная, указывающая, ожидает ли клиент
        self.client_done = threading.Event()  # Событие для синхронизации завершения обслуживания клиента

    def barber(self):
        while True:
            with self.lock:
                if self.client_waiting:  # Если клиент ждет
                    self.client_waiting = False  # Сброс флага ожидания клиента
                    self.client_done.set()  # Установка события о завершении обслуживания клиента
                    print("Barber is cutting hair")  # Парикмахер стрижет волосы
                    time.sleep(random.uniform(0.5, 1))  # Имитация времени стрижки
                    self.client_done.clear()  # Сброс события о завершении обслуживания клиента
                else:
                    self.barber_sleeping = True  # Парикмахер спит
                    print("Barber is sleeping")  # Парикмахер спит
                    self.lock.release()  # Освобождение мьютекса
                    print("11")
                    self.client_done.wait()  # Ожидание события о завершении обслуживания клиента
                    print("12")
                    self.lock.acquire()  # Захват мьютекса
                    self.barber_sleeping = False  # Парикмахер просыпается
                    print("Barber woke up")  # Парикмахер проснулся

    def client(self):
        while True:
            time.sleep(random.uniform(0.1, 0.5))  # Имитация времени до прихода клиента
            with self.lock:
                if self.barber_sleeping:  # Если парикмахер спит
                    print("Client wakes up barber")  # Клиент будит парикмахера
                    self.client_waiting = True  # Установка флага ожидания клиента
                    self.client_done.clear()  # Сброс события о завершении обслуживания клиента
                    self.lock.release()  # Освобождение мьютекса
                    self.client_done.wait()  # Ожидание события о завершении обслуживания клиента
                    self.lock.acquire()  # Захват мьютекса
                else:
                    if self.num_chairs > 0:  # Если есть свободные стулья
                        print("Client takes a seat")  # Клиент садится на стул
                        self.num_chairs -= 1  # Уменьшение количества свободных стульев
                        self.lock.release()  # Освобождение мьютекса
                        self.client_done.set()  # Установка события о завершении обслуживания клиента
                    else:
                        print("Client leaves, no chairs available")  # Клиент уходит, нет свободных стульев
                        self.lock.release()  # Освобождение мьютекса

if __name__ == "__main__":
    num_chairs = 3  # Количество стульев в парикмахерской
    barber_shop = BarberShop(num_chairs)  # Создание объекта парикмахерской
    barber_thread = threading.Thread(target=barber_shop.barber)  # Создание потока парикмахера
    clients = [threading.Thread(target=barber_shop.client) for _ in range(5)]  # Создание потоков клиентов

    barber_thread.start()  # Запуск потока парикмахера
    for client in clients:  # Запуск потоков клиентов
        client.start()

    barber_thread.join()  # Ожидание завершения работы потока парикмахера
    for client in clients:  # Ожидание завершения работы потоков клиентов
        client.join()

    print("end")

