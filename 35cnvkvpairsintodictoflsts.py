# convert seq of k,v pairs to dict of lsts
from collections import defaultdict
class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
dd_dict = defaultdict(list)
for classname,no in class_roll:
    dd_dict[classname].append(no)
print(dd_dict.items())
