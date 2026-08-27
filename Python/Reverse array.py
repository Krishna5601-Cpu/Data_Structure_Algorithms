def reverse_arr(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Array before reversing: ")
for i in nums:
    print(i)

reverse_arr(nums)


print("Array after reversing: ")
for i in nums:
    print(i)
