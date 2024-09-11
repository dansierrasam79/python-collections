#rotate list negative times
from collections import deque

init_dq = deque([2,4,6,8,10,12,14])
rotations = int(input("How many negative rotations?: "))
init_dq.rotate(-rotations)
print(init_dq)
