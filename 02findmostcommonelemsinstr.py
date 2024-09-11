# find most common elements in string
from collections import Counter
init_str = "lkseropewdssafsdfafkpwe"
cnt = Counter(init_str)
print(cnt.most_common(3))
