# remove duplicate words
from collections import OrderedDict
init_str = "Python Exercises Practice Solution Exercises"
init_lst = init_str.split(" ")
od = OrderedDict()
for word in init_lst:
    od[word] = word
final_str = ' '.join(od.keys())
print(final_str)
