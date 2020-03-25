'''
Highest Priority Word
Time Limit: 1 seconds
Memory Limit: 32 megabytes

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''


import re

power_alphabet = {
  ' ': 0,
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4,
  'e': 5, 
  'f': 6,
  'g': 7,
  'h': 8,
  'i': 9,
  'j': 10,
  'k': 11,
  'l': 12,
  'm': 13,
  'n': 14,
  'o': 15,
  'p': 16,
  'q': 17,
  'r': 18,
  's': 19,
  't': 20,
  'u': 21,
  'v': 22,
  'w': 23,
  'x': 24,
  'y': 25,
  'z': 26,
}

def filter_str():
  reg = re.compile('[^a-zA-Z ]')
  my_string = reg.sub('', input('enter your sentence: ').lower())
  my_list = my_string.split()
  return my_list

def max_value(my_list):
  
  count = 0
  res_list = []

  for element in my_list:
    for x in range(len(element)):
      count += power_alphabet[element[x]]
    res_list.append(count)
    count = 0
  return max(res_list)

print(max_value(filter_str()))
