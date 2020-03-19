def func(my_list):
  count = 0
  for x in range(1, len(my_list), 2):
    if my_list[x][0] >= my_list[count][0] and my_list[x][1] <= my_list[count][1]:
      my_list.pop(x)
      count += 1
    else:
      count += 1
      continue
  return my_list

print(func([(1,6), (2,5), (8, 10)]))
