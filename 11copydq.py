# copy dq object and check if shallow copy
from collections import deque
init_dq = deque([1, 3, 5, 7, 9])
print(id(init_dq))
sec_dq = init_dq.copy()
print(id(sec_dq))
print(id(init_dq[0]),id(sec_dq[0]))
