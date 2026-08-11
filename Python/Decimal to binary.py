num = int(input("Enter num: "))

ans = 0
i = 0

while num > 0:
    bit = num & 1
    ans = bit * (pow(10, i)) + ans
    i += 1
    num = num >> 1

print(ans)
