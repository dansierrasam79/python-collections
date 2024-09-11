#find most common words
from collections import Counter
text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""
text_lst = text.split(" ")
text_lst_final = []
for word in text_lst:
    if word[-1] in ".,';:":
        print(word[:-1])
        text_lst_final.append(word[:-1])
    else:
        text_lst_final.append(word)
cnt =Counter(text_lst_final)
print(cnt.most_common(10))
