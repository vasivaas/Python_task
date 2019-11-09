#Write a function that computes the volume of a sphere given its radius.
def vol(rad):
	pi = 2.14
	obem = (4/3.0)*2.14*(rad**3)
	return int(obem)
print vol(25)



#Write a function that checks whether a number is in a given range (Inclusive of high and low)
def bool_check(num, low, high):
	for element in xrange(low, high+1):
		if num == element:
			return True
			break
		else:
			return False
print bool_check(5,1,11)

#or not boolean

def ran_check(num, low, high):
	for element in xrange(low, high+1):
		if num == element:
			print 'this number {0} is in a given range'.format(num)
			break
	else:
		print 'a number is in a not given range'
print ran_check(5,4,7)

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def up_low(s):
	count_up = 0
	count_low = 0
	for index in xrange(len(s)):
		if s[index] == s[index].upper():
			count_up += 1
		elif s[index] == s[index].lower():
			count_low += 1
		else:
			pass
	print "No. of Upper case characters : {x}".format(x = count_up)
	print "No. of Lower case Characters :  {y}".format(y = count_low)
print up_low('HelloMrRogershowareyouthisfineTuesday')

#or use module - collections

from collections import Counter
import re
def up_low(s):
	count_upper = 0
	count_lower = 0
	words = re.split(' ', s)
	st = "".join(words)
	l = Counter(st)
	for k, val in l.iteritems():
		if k == k.upper():
			count_upper += l[k]
		elif k == k.lower():
			count_lower += l[k]
		else:
			pass
	print "No. of Upper case characters : {x}".format(x = count_upper)
	print "No. of Lower case Characters :  {y}".format(y = count_lower)
			
print up_low('Hello Mr Rogers how are you this fine Tuesday')

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
from collections import Counter
def unique_element(l):
	res = []
	element = Counter(l)
	for k in element:
		res.append(k)
	return res
print unique_element([1,1,1,1,2,2,3,3,3,3,4,5])

# or

def unique_elem(l):
	res = set(l)
	return list(res)
print unique_elem([1,1,1,1,2,2,3,3,3,3,4,5])

#or

def unique_elem(l):
	res = []
	start = l[0]
	for index in xrange(1, len(l)):
		if start != l[index]:
			res.append(start)
			start = l[index]
	res.append(l[-1])
	return res
print unique_elem([1,1,1,1,2,2,3,3,3,3,4,5,6,6,7,7,9])


#Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
	res = 1
	for num in numbers:
		res *= num
	return res
print multiply([1, 2, 3, -4, 2])

# or use lambda expression

print reduce(lambda x,y: x*y, [1, 2, 3, -4, 2])		


#Write a Python function that checks whether a passed string is palindrome or not.
def palindrome(s):
	st = "".join(reduce(lambda x,y : y+x, s))
	if st == s:
		return True
	else:
		return False
print palindrome('helleh')

#or

def palindrome(s):
	st = "".join(list(reversed(s)))
	if st == s:
		return True
	else:
		return False
print palindrome("ab") 

# or

def palindrome(s):
	st = lambda x: x[::-1]
	if st(s) == s:
		return True
	else:
		return False
print palindrome("aa")


#Write a Python function to check whether a string is pangram or not.
from collections import Counter

def ispangram(str1, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
	str1 = str1.lower()
	l = Counter("".join(str1.split()))
	count = 0
	for k in l:
		for elem in alphabet:
			if k == elem:
				count += 1
				break
	if count == len(alphabet):
		return True
	else:
		return False
print ispangram("The quick brown fox jumps over the lazy dog")
