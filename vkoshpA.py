n, m, k = [int (i) for i in input().split()]
if k > min(n, m):
	print ("impossible")
else:
	print ("possible")
	for i in range (k):
		print ("."*i, "*", "."*(m-i-1))
	for i in range (n-k):
		print("."*m)
