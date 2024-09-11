# break lists of ints to sets
def brk_lst(lst,no):
    count = 1
    final_lst = []
    temp_lst = []
    for item in lst:
        temp_lst.append(item)
        if count == no:
            final_lst.append(temp_lst)
            temp_lst = []
            count = 0
        count += 1
    return final_lst
#driver code
init_list = [1, 2, 3, 4, 5, 6, 7, 8,9]
div_no = 3
if len(init_list) % div_no == 0:
    print(brk_lst(init_list,div_no))
    print(True)
else:
    print(False)
