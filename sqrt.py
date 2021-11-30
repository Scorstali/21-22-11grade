n = int(input())
l = 0
r = n
for i in range (100):
	a = (l+r)/2
	if a*a > n:
		r = a
	else:
		l = a
	
print (a)
 
