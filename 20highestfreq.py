# find elem with highest frequency
from collections import Counter
cnt = Counter([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2])
print(cnt.most_common(1))
