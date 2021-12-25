n = int(input())
glass = ["a", "e", "i", "o", "u"]
c = [0]*n
ok = 0

for i in range (n):
	s = str(input()) + "s"
	k = 0
	for j in range(len(s)):
		if (s[j] in glass and j == len(s)) or (s[j] in glass and s[j+1] not in glass):
			k += 1
	c[i] = k
	


for t in range (n-1):
	x = 0
	y = 0
	k = 0
	while k < 17 and t < n:
		k += c[t]
		t += 1
		if k == 17:
			q = t - 1
			while x < 5:
				x += c[q]
				q -= 1
				if x == 5:
					while y < 7:
						y += c[q]
						q -= 1
						if y == 7:
							ok += 1

print (ok)
