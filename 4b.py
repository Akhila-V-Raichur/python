def ro2dec(romstr):
    rd={'I':1,"V":5,"X":10,'L':50,'C':100,'D':500,'M':1000}

    rb=list(romstr)[::-1]
    rv=rd[rb[0]]
    v=0
    for num in rb:
        lv=rd[num]
        if lv<rv:
            v-=lv
        else:
            v+=lv
        rv=lv
    return v
romstr=input("enter the roman:")
print("the decimal is:",ro2dec(romstr))
    