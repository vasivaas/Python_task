#Use for, split(), and if to create a Statement that will print out words that start with 's':
import re
st = 'Print only the words that start with s in this sentence'
l = re.split(' ', st)
result = [element for element in l if element[0] == 's'] #generacia lista
print result

#Use range() to print all the even numbers from 0 to 10.
mass = [num for num in range(0,11) if num%2 == 0]
print mass

#Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mas = [num for num in xrange(1,51) if num%3 == 0]
print mas

#Go through the string below and if the length of a word is even print "even!"
import re
s = 'Print every word in this sentence that has an even number of letters'
l = re.split(' ', s)

for element in l:
	if len(element) % 2 == 0:
		print "this element {x} - even".format(x=element)
	else:
		print "this element {x} - not even".format(x=element)

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the 
#multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".		

for num in xrange(1,101):
	if (num%3==0) and (num%5==0):
		print "FizzBuzz"
	elif num%3==0:
		print "Fizz"
	elif num%5==0:
		print "Buzz"
	else:
		print num

#Use List Comprehension to create a list of the first letters of every word in the string below:
import re
st_r = 'Create a list of the first letters of every word in this string'
l = re.split(' ', st_r.lower())
'''massive = []
for element in l:
	for index in xrange(len(element)):
		if index == 0:
			massive.append(element[index])'''
massive = [element[index] for element in l for index in xrange(len(element)) if index == 0]
print massive
