#find second lowest score
subjects_marks_list = [['Avik Das ', 89.0], ['ayan Roy', 75.0], ['Sayan Dutta', 93.0]]

marks_list = [item[1] for item in subjects_marks_list]

sort_marks = sorted(marks_list)

second_smallest_marks = sort_marks[1]

for lst in subjects_marks_list:
    if lst[1] == second_smallest_marks:
        print("Name: ", lst[0])
        print("Marks:", lst[1])
