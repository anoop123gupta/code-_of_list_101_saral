char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
a=[]
for i in char_list:
	if i not in a:
		a.append(i)
print a
for i in a:
	count=0
	for j in char_list:
		if i==j:
			count+=1
	if count>1:
		print "repeated", i, 'is', count , 'times'
