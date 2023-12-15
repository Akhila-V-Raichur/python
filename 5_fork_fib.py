import sys
import os
import subprocess

def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num
    print()

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <non-negative_integer>")
        return 1
    
    n = int(sys.argv[1])

    if n < 0:
        print("Error: The input should be a non-negative integer.")
        return 1

    pid = os.fork()

    if pid < 0:
        print("Error: Forking failed.")
        return 1
    elif pid == 0:
        # Child process
        print(f"Child process (PID: {os.getpid()}) Fibonacci Series: ", end="")
        generate_fibonacci(n)
    else:
        # Parent process
        print(f"Parent process (PID: {os.getpid()}) waiting for the child process (PID: {pid}) to finish...")
        os.wait()
        print("Parent process: Child process has finished.")

if __name__ == "__main__":
    main()
