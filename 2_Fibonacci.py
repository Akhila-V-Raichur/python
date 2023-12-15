import threading

def fibonacci_method1(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

n = int(input("Enter the number of terms in Fibonacci series: "))

if n<0:
    raise Exception("Negative number not allowed")

t1=threading.Thread(target=print, args=(fibonacci_method1(n),))
t1.start()
t1.join()
