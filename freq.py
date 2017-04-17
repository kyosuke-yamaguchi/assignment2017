import sys
from collections import Counter

f = open(sys.argv[1])

line = f.read()

r = line.replace("\n"," ")

split = r.split(" ")

c = Counter(split)

for k,v in sorted(c.items(), key=lambda x: x[1], reverse=True):

    print (k,v)
