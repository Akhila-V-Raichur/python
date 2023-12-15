import random
def ms(lst):
    if len(lst)>1:
        m=len(lst)//2
        lh=lst[:m]
        rh=lst[m:]
        ms(lh)
        ms(rh)
        i=j=k=0
        while i<len(lh) and j<len(rh):
            if lh[i]<rh[j]:
                lst[k]=lh[i]
                i+=1
            else:
                lst[k]=rh[j]
                j+=1
            k+=1
        while i<len(lh):
            lst[k]=lh[i]
            i+=1
            k+=1
        while j<len(rh):
            lst[k]=rh[j]
            j+=1
            k+=1
        return lst
def ins(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

ml=[]
for i in range(10):
    ml.append(random.randint(0,999))
print("unsorted list")
print(ml)
print("sorted using merge:")
ms(ml)
print(ml)

ml=[]
for i in range(10):
    ml.append(random.randint(0,999))
print("unsorted list")
print(ml)
print("sorted using insertion:")
ins(ml)
print(ml)
