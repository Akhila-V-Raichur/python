s1=input("enter the string 1:")
s2=input("enter string 2:")
s=min(len(s1),len(s2))
m=max(len(s1),len(s2))
c=0
for i in range (s):
    if(s1[i]==s2[i]):
        c+=1
sp=(c/m)*100
print("the similarity is:")
print(round(sp,2),"%")
