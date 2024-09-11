from collections import Counter
lst = ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
cnt = Counter(lst)
print(cnt.most_common())