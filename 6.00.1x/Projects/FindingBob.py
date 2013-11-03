s1 = False
s2 = False
count = 0

for letter in s:
	if letter == 'b':
		if s1 == True and s2 == True:
			count += 1
			s2 = False
		else:
			s1 = True
	elif letter == 'o':
		if s1 == True and s2 == False:
			s2 = True
		else: 
			s1 = False
			s2 = False
	else:
		s1 = False
		s2 = False 

print ("Number of times bob occurs is " + str(count))
