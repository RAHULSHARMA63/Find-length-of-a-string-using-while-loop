def findLen(str):
	counter = 0
	while str[counter:]:
		counter += 1
	return counter

str = "Vaishali Sharma"
print(findLen(str))