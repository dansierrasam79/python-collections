from collections import defaultdict
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dd = defaultdict(list)
for key, val in colors:
    dd[key] = val
print(dd)