# display distinct words and number of occurrences
from collections import Counter,OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

#Driver code
words = ["Red", "Blue","Green","Red","Green","Blue","Black","White","Black","White"]

cnt = OrderedCounter(words)
print(cnt)
print(len(cnt))

for wrd in cnt:
    print(cnt[wrd],end=" ")
