arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search = int(input("Enter the number to search: "))
linear_count = 0
linear_found = False

for i in range(len(arr)):
    linear_count += 1
    if arr[i] == search:
        print("Linear Search:")
        print("Element found at index:", i)
        print("Comparisons:", linear_count)
        linear_found = True
        break

if linear_found == False:
    print("Linear Search:")
    print("Element not found.")
    print("Comparisons:", linear_count)

low = 0
high = len(arr) - 1
binary_count = 0
binary_found = False

while low <= high:
    binary_count += 1
    mid = (low + high) // 2

    if arr[mid] == search:
        print("\nBinary Search:")
        print("Element found at index:", mid)
        print("Comparisons:", binary_count)
        binary_found = True
        break
    elif search < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if binary_found == False:
    print("\nBinary Search:")
    print("Element not found.")
    print("Comparisons:", binary_count)
