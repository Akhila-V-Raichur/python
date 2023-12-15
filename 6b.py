import os
import sys
import pathlib
import zipfile

dirname=input("enter the dir u wanna backup:")
if not os.path.isdir(dirname):
    print("the dir doesnt exist.")
    sys.exit(0)

indir=pathlib.Path(dirname)
with zipfile.ZipFile("myZip.zip",mode="w")as archive:
    for filepath in indir.rglob("*"):
        archive.write(filepath,archname=filepath.relative_to(indir))

if os.path.isfile("myZip.zip"):
    print("archieve""myZip.zip""created successfully")
else:
    print("not able to create")