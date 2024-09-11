#find difference between two lists
from collections import Counter
lst = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lst2 = [1, 1, 2, 4, 5, 6]

cnt = Counter(lst)
cnt2 = Counter(lst2)

diff = cnt - cnt2
print(list(diff.elements()))
