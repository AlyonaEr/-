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
            r = random.randint(50, 500)
            self.balance += r
            print(f'Пополнение: {r}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        self.lock.acquire()
        for i in range(100):
            r = random.randint(50, 500)
            print(f'Запрос на {r}')
            if r <= self.balance:
                self.balance -= r
                print(f'Снятие: {r}. Баланс: {self.balance}')
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
