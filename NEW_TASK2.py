'''
A digital root is the recursive sum of all the digits in a number. 
Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
This is only applicable to the natural numbers.
'''

import functools

def my_func(num_in):
  arr = list(num_in)
  res = str(functools.reduce(lambda x, y: int(x) + int(y), arr))
  if len(res) == 1:
    return res
  else:
    return my_func(res)

num_in = input('enter a natural number: ')
print(my_func(num_in))
