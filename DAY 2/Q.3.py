
size = int(input("Enter the size of the array: "))
arr = []

for i in range(size):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter the number to search: "))

found = False
for i in range(size):
    if arr[i] == search:
        print("Element found at index:", i)
        found = True
        break
if found == False:
    print("Element not found.")
