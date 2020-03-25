'''
  Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

  Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

  If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Input

  Input consists of one line.

  First Line is having a string.

Output

  Output should also be string but with an sorted manner.
'''

import re

my_str = input('enter your sentence: ')

def sort_arr(arr):
  return arr.sort()

def str_to_arr(string):
  return string.split()

def sorting_into_strings(my_str):

  num_list = re.findall('(\d+)', my_str)
  '''for index in range(len(num_list)):
    num_list[index] = int(num_list[index])'''
  sort_arr(num_list)

  my_str = str_to_arr(my_str)
  
  for index in range(len(my_str)):
    for x in range(len(num_list)):
      if num_list[x] in my_str[index]:
        num_list[x] = my_str[index]
  return num_list

print(sorting_into_strings(my_str))
