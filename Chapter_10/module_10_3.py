import threading
import random
import time


class Bank:
    DEPOSIT_TIMES = 100
    MIN_AMOUNT = 50
    MAX_AMOUNT = 500
    SLEEP_TIME = 0.001

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit_money(self):
        for _ in range(self.DEPOSIT_TIMES):
            amount = random.randint(self.MIN_AMOUNT, self.MAX_AMOUNT)
            self.balance += amount
            print(f"Deposited: {amount}. Balance: {self.balance}")
            self._check_release_lock()
            time.sleep(self.SLEEP_TIME)

    def withdraw_money(self):
        for _ in range(self.DEPOSIT_TIMES):
            amount = random.randint(self.MIN_AMOUNT, self.MAX_AMOUNT)
            print(f"Withdrawal request: {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: {amount}. Balance: {self.balance}")
            else:
                print("Request denied, insufficient funds")
                self.lock.acquire()

    def _check_release_lock(self):
        if self.balance >= self.MAX_AMOUNT and self.lock.locked():
            self.lock.release()

def main():
    bank = Bank()
    deposit_thread = threading.Thread(target=bank.deposit_money)
    withdraw_thread = threading.Thread(target=bank.withdraw_money)
    deposit_thread.start()
    withdraw_thread.start()
    deposit_thread.join()
    withdraw_thread.join()

if __name__ == '__main__':
    main()
