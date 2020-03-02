#0
def move_zero_to_end(l):
	for index in range(len(l) - 1):
		for el in range(len(l) - 1 - index):
			print l
			if(l[el] == 0  and l[el+1] != 0):
				l[el], l[el+1] = l[el+1], l[el]
	return l
	
print move_zero_to_end([0,1, 0,0,3,1,2])
print move_zero_to_end([10,1,0,3,1,0,0,0,2])

#1
def python_helpers(nums):
	pos = 0
        
	for i in range(len(nums)):
		el = nums[i]
		if el != 0:
			nums[pos], nums[i] = nums[i], nums[pos]
			pos += 1
	print(nums)

python_helpers([10,1,0,3,1,0,0,0,2])

#2
a = [0,1,0,3,12]


B=list(filter(lambda x: x != 0, a))
B.extend([0]*a.count(0))


B=[x for x in a if x != 0]
B.extend([0]*a.count(0))
