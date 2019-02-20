# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# max1=0
# for i in numbers:
# 	if i>max1:
# 		max1=i
# print max1
# --------------second method--------
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max1=0
i=0
l=len(numbers)
while i<l:
	if numbers[i]>max1:
		max1=numbers[i]
	i+=1
print max1