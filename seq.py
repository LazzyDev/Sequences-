
import math

for num in range (1,11):
	if (num%2==0):
		num = ((5**num)+0)
		print(num," ")
	else:
		num = ((5**num)+num)
		print(num," ")
