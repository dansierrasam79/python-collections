# extend deque with more elements from iterable
from collections import deque
second_list = [12, 14, 16, 18, 20]
init_dq = deque([2, 4, 6, 8, 10])
init_dq.extend(second_list)
print(init_dq)
