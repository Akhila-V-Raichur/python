n=int(input("enter the number:"))
temp=n
new=rem=0
arr=[0]*10
while temp!=0:
    rem=temp%10
    arr[rem]=arr[rem]+1
    new=new*10+rem
    temp=temp//10
if new==n:
    print("palindrome")
else:
    print("not palindrome")
    print("the occurences of digit as followws")
for i in range(0,10):
    print("the digit",i,"appears",arr[i],"times.")