# find classwise roll no from tup of tups
from collections import defaultdict
classes = (('V', 1),('VI', 1),('V', 2),('VI', 2),('VI', 3),('VII', 1),)
roll_nos = defaultdict(list)

for classno,num in classes:
    roll_nos[classno].append(num)

print(roll_nos)
