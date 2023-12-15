import os.path
import sys
fname=input("enter the file name:")
if not os.path.isfile(fname):
    print("the file doesnt exist")
    sys.exit(0)

infile=open(fname)
ll=infile.readlines()
for i in range(10):
    print(i+1,":",ll[i])

word=input("enter the word")
count=0
for line in ll:
    count+=line.count(word)
print("the word",word,"appears",count,"times.")

