dict = { ']' : '[',
		 ')' : '(',
		 '}' : '{',
}

def check_valid_st(st):
	l = []
	
	for element in st:
		if element in dict.values():
			l.append(element)
		elif element in dict and dict[element] == l[len(l)-1]:
			l.pop()
		else: return False
		
	return not l
	
print check_valid_st('{()}[]')
