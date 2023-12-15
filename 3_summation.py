import threading

def calculate_sum(n, result):
    total = 0
    for i in range(1, n + 1):
        total += i
    result[0] = total

n = int(input("Enter a nonnegative integer: "))

if n<0:
    raise Exception("Negative number not allowed")

result = [0]  # A object to hold the result

sum_thread = threading.Thread(target=calculate_sum, args=(n, result))
sum_thread.start()
sum_thread.join()

print(f"The summation of the first {n} numbers is: {result[0]}")

