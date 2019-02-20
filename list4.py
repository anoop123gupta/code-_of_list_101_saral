numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max2=0
max1=0
i=0
l=len(numbers)
while i<l:
	if numbers[i]>max1:
		max1=numbers[i]
	if numbers[i]>max2 and max1!=numbers[i]:
		max2=numbers[i]
	i+=1
print max2