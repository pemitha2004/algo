
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search = int(input("Enter the number to search: "))

low = 0
high = len(arr) - 1
comparisons = 0
found = False

while low <= high:
    comparisons += 1
    mid = (low + high) // 2

    if arr[mid] == search:
        print("Element found at index:", mid)
        print("Number of comparisons:", comparisons)
        found = True
        break
    elif search < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
if found == False:
    print("Element not found.")
    print("Number of comparisons:", comparisons)
