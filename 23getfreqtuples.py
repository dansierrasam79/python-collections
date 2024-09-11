# get freq of tuples
from collections import Counter
int_lst = [['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7']]
fin_lst = [tuple(sorted(lst)) for lst in int_lst]
result = Counter(fin_lst)
for k,v in result.items():
    print(k, " ",v)
