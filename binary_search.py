# Python Program for recursive binary search. 
def binarySearch(arr, low, high, key):

    mid = (low + high) / 2

    if high >= low:
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarySearch(arr, low, mid - 1, key)
        elif arr[mid] < key:
            return binarySearch(arr, mid + 1, high, key)

    else:
        # Element is not present in the array
        return -1


# driver code
if __name__ == "__main__":
    # Test array
    input_arr = [2, 3, 4, 10, 40, 0]
    key = 10

    result = binarySearch(input_arr, 0, len(input_arr) - 1, key)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")
