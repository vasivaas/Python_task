'''
  Дан массив arr [] целых положительных чисел размера N. Обратно каждый подмассив из K групповых элементов.

Входные данные:
Первая строка ввода содержит одно целое число T, обозначающее количество тестовых случаев. Затем следуют тесты T. Каждый тестовый набор состоит из двух строк ввода.
Первая строка каждого теста состоит из целого числа N (размер массива) и целого числа K, разделенных пробелом. Вторая строка каждого теста содержит N целых чисел, разделенных пробелом, обозначающих элементы массива.

Выход:
Для каждого теста выведите измененный массив.
'''
count = 0
T = int(input('enter the number of tests: '))
while count < T:
  N = int(input('enter size of array: '))
  K = int(input('enter the array delimiter: '))
  arr = []
  while len(arr) < N:
    tmp = int(input("enter elements for array: "))
    arr.append(tmp)

  def n_split(iterable, n):
    num_extra = len(iterable) % n
    zipped = list(zip(*[iter(iterable)] * n))
    return zipped if not num_extra else zipped + [iterable[-num_extra:], ]
  new_arr = []
  for ints in n_split(arr, K):
    k = [(i) for i in ints]
    k.reverse()
    new_arr += k
  print(new_arr)
  count += 1
