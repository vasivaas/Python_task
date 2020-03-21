'''
Find First and Last Position of Element in Sorted Array
'''
def bubble(array):
  for i in range(len(array)-1):
    for j in range(len(array)-i-1):
      if array[j] > array[j+1]:
        buff = array[j]
        array[j] = array[j+1]
        array[j+1] = buff
  return array

def find_index(array, target):
  count=0
  new_arr=[]
  for element in array:
    if element == target:
      new_arr.append(count)
      count += 1
    else:
      count += 1 
  if len(new_arr) == 0:
    new_arr = [-1,-1]
  else:
    first_i, last_i = new_arr [0], new_arr[len(new_arr)-1]
    new_arr = [first_i, last_i]
  return new_arr

N = int(input('enter size of array: '))
target = int(input('enter target: '))
arr = []
while len(arr) < N:
  tmp = int(input("enter elements for array: "))
  arr.append(tmp)
bubble(arr)
print(find_index(arr, target))

