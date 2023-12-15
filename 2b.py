def bin2dec(binary):
    decimal=0
    i=0
    while binary!=0:
        dec=binary%10
        decimal=decimal+dec*pow(2,i)
        binary=binary//10
        i+=1
    print(decimal)
    return(decimal)

def oct2dec(octal):
    decimal2=0
    i=0
    while octal!=0:
        dec2=octal%10
        decimal2=decimal2+dec2*pow(8,i)
        octal=octal//10
        i+=1
    print(decimal2)
    return(decimal2)

def dectohex(n):
    hdn=""
    while n!=0:
        temp=0
        temp=n%16
        if temp<10:
            hdn=str(temp)+hdn
        else:
            hdn=chr(temp+87)+hdn
        n=n//16
    return hdn
bd=int(input("enter bin num"))
bdobj=bin2dec(bd)
print("the decimal is:",bdobj)
od=int(input("enter octal num"))
odobj=oct2dec(od)
print("the decimal is:",odobj)
hex=dectohex(odobj)
print("the hexadecimal is",hex)

