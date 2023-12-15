def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
n=int(input("enter the number:"))
if n<0:
    print("invalid input")
else:
    print("the first ",n,"fibonacci series:")
for i in range(n):
    print(fib(i))