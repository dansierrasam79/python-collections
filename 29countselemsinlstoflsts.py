from collections import Counter
lsts = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
final_lst = [item for lst in lsts for item in lst]
cnt = Counter(final_lst)
print(cnt.most_common())