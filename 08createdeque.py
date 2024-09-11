# create deque from tuple and list iterables
from collections import deque
init_tuple = (2, 4, 6)
init_list = [2, 2, 4, 6, 8, 10, 12]
init_dq = deque(init_tuple)
second_dq = deque(init_list)

print(init_dq)
print(second_dq)
