# compare two lists
from collections import Counter
n1 = [20, 10, 30, 10, 20, 30]
n2 = [30, 20, 10, 30, 20, 50]
print(Counter(n1) == Counter(n2))
