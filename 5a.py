import re
def ipn(ns):
    if len(ns)!=12:
        return False
    for i in range(len(ns)):
        if i==3 or i==7:
            if ns[i]!="-":
                return False
        else:
            if ns[i].isdigit()==False:
                return False
    return True
def cpn(ns):
    pnp=re.compile('\d{3}-\d{3}-\d{4}')
    if pnp.match(ns):
        return True
    else :
        return False 

phnum=input("enter the number:")
print("without using regular expression:")
if ipn(phnum):
    print("valid")
else:
    print("invalid")

print("with using regular expression:")
if cpn(phnum):
    print("valid")
else:
    print("invalid")


