import os
import sys

filename = sys.argv

def gitUpload(filename):
    print(os.system(f"git add ."))
    print(os.system(f"git commit -m 'added'"))
    print(os.system("git push -u web main --force"))
    print(os.system("git status"))


gitUpload(filename[1])
