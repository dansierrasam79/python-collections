# find the elements appearing max times
from collections import Counter
cnt = Counter([10, 10, 20, 30, 40, 10, 20, 10])
print(cnt.most_common(1))
