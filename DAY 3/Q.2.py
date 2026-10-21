arr = [25, 15, 30, 10, 20]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key

    print("Pass", i, ":", arr)

print("Final sorted array:", arr)
