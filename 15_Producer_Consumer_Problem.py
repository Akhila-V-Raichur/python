import threading as th
import random
import time

class Buffer:
    def __init__(s, capacity):
        s.capacity = capacity
        s.buffer = []
        s.mutex = th.Semaphore()
        s.full = th.Semaphore(0)
        s.empty = th.Semaphore(s.capacity)

    def produce(s):
        return random.randint(1, 1000)

    def consume(s):
        pass

    def producer_thread(s, total_items):
        items_produced = 0
        while items_produced < total_items:
            s.empty.acquire()
            s.mutex.acquire()

            item = s.produce()
            s.buffer.append(item)
            print(f"Item no.{items_produced + 1} Produced: {item}")

            s.mutex.release()
            s.full.release()

            s.mutex.acquire()
            items_produced += 1
            s.mutex.release()



    def consumer_thread(s, total_items):
        items_consumed = 0
        while items_consumed < total_items:
            s.full.acquire()
            s.mutex.acquire()

            s.consume()
            item = s.buffer.pop(0)
            print(f"Item no.{items_consumed + 1} Consumed: {item}")

            s.mutex.release()
            s.empty.release()

            s.mutex.acquire()
            items_consumed += 1
            s.mutex.release()

            

Buffer_Capacity = 5
Total_Items = 10

buffer = Buffer(Buffer_Capacity)

producer_thread = th.Thread(target=buffer.producer_thread, args=(Total_Items,))
consumer_thread = th.Thread(target=buffer.consumer_thread, args=(Total_Items,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
