def search(arr, target):
    """Linear search to find target in array"""
    for element in arr:
        if element == target:
            return True
    return False


def main():
    # Get array size with validation
    while True:
        try:
            arr_size = int(input("Enter array size: "))
            if arr_size > 0:
                break
            print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid integer")

    # Get array elements
    nums_arr = []
    print("Enter array elements:")
    for i in range(arr_size):
        while True:
            try:
                element = int(input(f"Element {i+1}: "))
                nums_arr.append(element)
                break
            except ValueError:
                print("Please enter a valid integer")

    # Get target
    while True:
        try:
            target = int(input("Enter target: "))
            break
        except ValueError:
            print("Please enter a valid integer")

    # Search and display result
    found = search(nums_arr, target)

    if found:
        print("Target is present in array")
    else:
        print("Target was not found in array")


if __name__ == "__main__":
    main()
