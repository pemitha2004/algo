size = int(input("Enter the size of the array: "))
arr = []

for i in range(size):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter the number to search: "))

low = 0
high = size - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == search:
        print("Element found at index:", mid)
        found = True
        break
    elif search < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found == False:
    print("Element not found.")
