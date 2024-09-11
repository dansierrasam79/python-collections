# calculate max aggregate of given tuple
from collections import defaultdict
lst = [('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]
dd_dict = defaultdict(int)

for k,v in lst:
    dd_dict[k] += v
        
print(max(dd_dict.items(),key=lambda x: x[1]))
