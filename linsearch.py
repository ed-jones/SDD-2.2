"Linear Search"

def lin(arr):
    "Performs linear search"
    inp = input()
    i = 0

    while i < len(arr):

        if arr[i] == int(inp):
            print("true")
            break

        i += 1
        if i == len(arr):
            print("false")

lin([1, 4, 2, 3, 8, 4, 12])
