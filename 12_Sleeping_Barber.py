import threading as th
import time
import random

class BarberShop:
    def __init__(s, num_chairs):
        s.num_chairs = num_chairs
        s.customers_waiting = []
        s.barber_busy = False
        s.mutex = th.Semaphore(1)
        s.customer_ready = th.Semaphore(0)
        s.barber_ready = th.Semaphore(0)

    def barber(s):
        while True:
            s.customer_ready.acquire()  # Wait for a customer
            s.mutex.acquire()
            customer = s.customers_waiting.pop(0)
            s.mutex.release()

            print(f"Barber is cutting hair of customer {customer}")
            time.sleep(1)
            print(f"Barber has finished cutting hair of customer {customer}")
            s.barber_ready.release()

    def customer(s, customer_id):
        s.mutex.acquire()
        if len(s.customers_waiting) < s.num_chairs:
            print(f"Customer {customer_id} enters the shop.")
            
            s.customers_waiting.append(customer_id)
            s.customer_ready.release()
            s.mutex.release()
            s.barber_ready.acquire()
            print(f"Customer {customer_id} leaves after getting a haircut.")
        else:
            print(f"Customer {customer_id} leaves because the shop is full.")
            s.mutex.release()


num_chairs = 3
num_customers = 5

shop = BarberShop(num_chairs)

barber_thread = th.Thread(target=shop.barber)
barber_thread.start()

customer_threads = []
for i in range(num_customers):
    customer_thread = th.Thread(target=shop.customer, args=(i,))
    customer_threads.append(customer_thread)

for thread in customer_threads:
    thread.start()

for thread in customer_threads:
    thread.join()

barber_thread.join()


