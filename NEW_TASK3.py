'''
Some numbers have funny properties. For example:
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p 
is equal to k * n.
In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
If it is the case we will return k, if not return -1.
Note: n and p will always be given as strictly positive integers.

'''

import functools

count = 0
T = int(input('enter the number of tests: '))
arr = []
while count < T:
  N = input('enter a number: ')
  if N[0] == '-':
    N = input('sorry, enter positive a number: ')
  arr = [int(x) for x in N]
  k = int(input('enter k: '))
  tmp=k
  new_arr = []
  for el in arr:
    new_arr.append(el**tmp)
    tmp += 1
  res = str(functools.reduce(lambda x, y: int(x) + int(y), new_arr))
  res2 = int(N)*k
  print(int(res)//int(N)) if int(res)==res2 else print('-1')
  count += 1
