#find chars less than 3
from collections import Counter
init_list = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
final_list = []
for init_str in init_list:
    cnt = Counter(init_str)
    final_list.append(cnt.most_common())

final_dict = {}
for lst in final_list:
    for tup in lst:
