# count students in class
from collections import Counter
classes = (('V', 1),('VI', 1),('V', 2),('VI', 2),('VI', 3),('VII', 1),)

stud_count = Counter(clnm for clnm,roll_no in classes)
print(stud_count)
