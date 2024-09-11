#rotate list
from collections import deque

init_dq = deque([2,4,6,8,10])
rotations = int(input("How many rotations?: "))
init_dq.rotate(rotations)
print(init_dq)
