from threading import Thread, Lock
import random
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.lock.acquire()

    def deposit(self):
        for i in range(100):
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            random_numbers = random.randint(50, 500)
            self.balance += random_numbers
            print(f'Пополнение: {random_numbers}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        self.lock.acquire()
        for i in range(100):
            random_numbers = random.randint(50, 500)
            print(f'Запрос на {random_numbers}')
            if random_numbers <= self.balance:
                self.balance -= random_numbers
                print(f'Снятие: {random_numbers}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
