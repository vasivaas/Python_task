#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран;
'''sum=0
for i in range(1, 101):
		sum += i
print sum'''

#Даны три числа. Вывести на экран «yes«, если среди них есть одинаковые, иначе вывести “ERROR”;
'''num1 = raw_input("enter first number:  ")
num2 = raw_input('enter second number:  ')
num3 = raw_input('enter third number:  ')

list = [int(num1), int(num2), int(num3)]

for n in list:
	if n == (list[0] or list[1] or list[2]):
		print "yes"
	else: 
		print "EROR"'''
		
#Даны три числа. Вывести на экран «yes«, если можно взять какие-то два из них и в сумме получить третье
'''max = 0
sum = 0

num1 = raw_input("enter first number:  ")
num2 = raw_input('enter second number:  ')
num3 = raw_input('enter third number:  ')

list = [int(num1), int(num2), int(num3)]

for n in range(len(list)):
	if list[n] > max:
		max = list[n]
		maxIndex = n
print "max element - {0}. his index - {1}".format(max, maxIndex)
max = list.pop(maxIndex)
for i in range(len(list)):
	sum += list[i]
if max == sum:
	print "Yes"
else:
	print "stupid"'''

#Дано три числа. Найти количество положительных чисел среди них;
'''count = 0
num1 = raw_input('Enter first number:  ')
num2 = raw_input('Enter second number:  ')
num3 = raw_input('Enter third number:  ')
list = [int(num3), int(num2), int(num3)]

for index in range(len(list)):
	if list[index] > 0:
		count += 1
	elif list[index] == 0:
		count -= 1
print count'''

#Вывести на экран все чётные значения в диапазоне от 1 до 497
'''for num in range(1, 498):
	if num % 2 == 0:
		print num'''

#Перемножить все не чётные значения в диапазоне от 0 до 9435;
'''list = [s for s in range(0, 9436)]
l = []
for num in range(len(list)):
	if list[num] % 2 != 0:
		l.append(list[num])
multi = 1
for s in l:
	multi *= s
print multi	'''

#Записать в массив все числа в диапазоне от 54 до 9184 кратные 5
'''l = [num for num in range(54, 9185) if num%5==0]
print l'''

#Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована;
'''for s in range(1,6):
	str = "0"*s
	print '{0}. {1}'.format(s, str)'''
'''	
d = {'х': "-.-",
	 'у': "--.",
	 'й': "..-"}
result = []
for el in ["х", "У", "й"].lower():
	result.append(d[el])
	
print result
'''
	
'''	
l1 = [1, 3, 4]
l2 = [4, 0, 5]

L = list(map(lambda x,y: x+y, l1,l2))
print L
'''

l1 = [1, 5, 2, 9, 3, 7]
l = list(map(sorted(), l1))
