my_list = [3,6,9,2,6]
max_elem = max(my_list)
x = list(map(lambda x: max_elem - x, my_list))
print(x) 
