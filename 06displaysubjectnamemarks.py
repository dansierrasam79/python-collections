#display subject name and marks
from collections import OrderedDict
subject_dict = OrderedDict()

subjects_marks = ["Bengali 58","English 62","Math 68"]
for item in subjects_marks:
    subject,marks = item.split(" ")
    if subject not in subject_dict:
        subject_dict[subject] = marks

print(subject_dict)
