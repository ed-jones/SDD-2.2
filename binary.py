import math

A = [1,5,6,10,15,16,17,20]

def binsearch(A):
	print("Enter input:")
	T = input()
	L = 0
	R = len(A) - 1
	m = int(math.floor((L+R)/2))
	while A[m] != T and m > 0:
		if  A[m] < T:
			m+=1
		elif A[m] > T:
			m-=1
	if A[m] != T:
		m = "not found"
	return m

print(binsearch(A))