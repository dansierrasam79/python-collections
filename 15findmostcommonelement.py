#most common element in deque
from collections import Counter
cnt_obj = Counter(['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python'])
print(cnt_obj.most_common(1))
