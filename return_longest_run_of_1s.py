'''
  Return the longest run of 1s for a given integer n 's binary representation.

  Example:Input: 242
  Output: 4
'''
def des_to_bin(x):
    if x == 0:
        return '0'
    res = ''
    while x > 0:
        res = ('0' if x % 2 == 0 else '1') + res
        x //= 2
    return res

def arr_sequence_one(arr):
  my_string = ''
  new_arr = []
  for element in arr:
    if element == '1':
      my_string += element
      continue
    else:
      new_arr.append(my_string)
      my_string = ''
      continue
  return new_arr

def max_count_sequence(arr):
  for el in range(len(arr)):
    arr[el] = arr[el].count('1')
  return max(arr)


num = int(input('enter a number: '))
bin_num = des_to_bin(num)
bin_list = [element for element in bin_num]
print(max_count_sequence(arr_sequence_one(bin_list)))
