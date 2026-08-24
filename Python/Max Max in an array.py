def getMax(arr):
    max_val = float("-inf")
    for i in range(len(arr)):
        if arr[i] >= max_val:
            max_val = arr[i]
    return max_val


def getMin(arr):
    min_val = float("inf")
    for i in range(len(arr)):
        if arr[i] <= min_val:
            min_val = arr[i]
    return min_val


# Taking user input
size = int(input("Enter the array size: "))
print("Enter array elements:")

num = []
for i in range(size):
    num.append(int(input()))

maximum = getMax(num)
minimum = getMin(num)
print(f"Max: {maximum} Min: {minimum}")
