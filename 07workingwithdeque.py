#work with deque
from collections import deque
init_dq = deque(['Red', 'Green', 'White'])
print(init_dq)
init_dq.appendleft("Pink")
print(init_dq)
init_dq.append("Orange")
print(init_dq)
init_dq.pop()
print(init_dq)
init_dq.popleft()
print(init_dq)
init_dq.reverse()
print(init_dq)
