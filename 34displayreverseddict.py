# display reversed Ordered Dict
from collections import OrderedDict
init_dict = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
od_dict = OrderedDict(init_dict.items())
for key, value in od_dict.items():
    print(key,value)
print("blah!")
for key in reversed(od_dict):
    print(key,od_dict[key])
