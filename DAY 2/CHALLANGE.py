arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

search = int(input("Enter the number to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    print("Middle element checked:", arr[mid])

    if arr[mid] == search:
        print("Element found!")
        print("Array Index:", mid)
        print("Position:", mid + 1)
        found = True
        break

    elif search < arr[mid]:
        high = mid - 1

    else:
        low = mid + 1

if found == False:
    print("Element not found.")
