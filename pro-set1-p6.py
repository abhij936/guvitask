n = int(input())
L = [ int(x) for x in input().split()]
count = 0
for i in range(0,n-2) :
	for j in range(i+1, n-1):
		for k in range(j+1, n ):
			if L[i] < L[j] < L[k] :
				count += 1
print(count)
