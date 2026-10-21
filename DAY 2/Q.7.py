arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:

    search = int(input("Enter the number to search: "))

    low = 0
    high = len(arr) - 1
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

    choice = input("Do you want to search again? (yes/no): ")

    if choice.lower() != "yes":
        print("Program Ended.")
        break
