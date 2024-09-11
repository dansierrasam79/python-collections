#remove elements from dq
from collections import deque
init_dq = deque([1,3,5,7,9])
print(len(init_dq))
init_dq.clear()
print("After removing all elements: ",len(init_dq))
