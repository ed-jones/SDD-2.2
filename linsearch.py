arr = [1,4,2,3,8,4,12]

def lin(arr):
	inp = input()
	i  = 0

	while i < len(arr):

		if arr[i] == int(inp):
			print "true"
			break

		i += 1
		if i == len(arr):
			print "false"

lin(arr)