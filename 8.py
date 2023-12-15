class palistr:
    def __init__(self):
        self.isPali=False
    def chkpalindrome(self,mystr):
        if mystr==mystr[::-1]:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali
class paliint(palistr):
    def __init__(self):
        self.isPali=False
    def chkpalindrome(self,val):
        temp=val
        rev=0
        while temp!=0:
            dig=temp%10
            rev=(rev*10)+dig
            temp=temp//10
        if rev==val:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali
    
st=input("enter the string:")
stobj=palistr()
if stobj.chkpalindrome(st):
    print("palindrome")
else:
    print("not palindrome")
it=int(input("enter the integer:"))
itobj=paliint()
if itobj.chkpalindrome(it):
    print("palindrome")
else:
    print("not palindrome")

