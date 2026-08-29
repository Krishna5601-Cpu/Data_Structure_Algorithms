def find_unique(arr):
    ans = 0
    for num in arr:
        ans ^= num  # XOR operator in Python
    return ans
