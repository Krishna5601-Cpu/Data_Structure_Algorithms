def swap_alternate(arr):
    for i in range(0, len(arr), 2):
        if (i + 1) < len(arr):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


# Taking user input
print("Enter array elements (10 numbers): ")
nums_arr = []

for i in range(10):
    nums_arr.append(int(input()))

print("\nBefore swap:")
for num in nums_arr:
    print(num)

swap_alternate(nums_arr)

print("\nAfter swap:")
for num in nums_arr:
    print(num)
