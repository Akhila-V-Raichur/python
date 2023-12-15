n=input("enter the sentence:")
wl=n.split()
print("the sentence has",len(wl),"words")
digcnt=lowcnt=upcnt=0
for ch in n:
    if '0'<=ch<='9':
        digcnt+=1
    elif 'A'<=ch<='Z':
        upcnt+=1
    elif 'a'<=ch<='z':
        lowcnt+=1
print("it has",digcnt,"digits",lowcnt,"lower",upcnt,"upper")