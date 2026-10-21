
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search = int(input("Enter the number to search: "))

found = False
for i in range(len(numbers)):
    if numbers[i] == search:
        print("Element found at index:", i)
        found = True
        break
if found == False:
    print("Element not found.")
