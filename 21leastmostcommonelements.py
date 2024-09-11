# most and least common letter in "hello world"
from collections import Counter
cnt = Counter("hello world")
counts =  cnt.most_common()
print(counts[0],counts[2])
