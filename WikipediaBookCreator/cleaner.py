import glob
import os

for f in glob.glob("*.pdf"):
    os.remove(f)
    print(f + " removed")