from collections import Counter
words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]
cnt = Counter(words)
print(cnt.most_common(3))