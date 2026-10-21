def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result = result + left[i:]
    result = result + right[j:]

    return result


numbers = [45, 12, 36, 8, 27, 19]

insertion_array = numbers.copy()
merge_array = numbers.copy()

insertion_result = insertion_sort(insertion_array)
merge_result = merge_sort(merge_array)

print("Insertion Sort:", insertion_result)
print("Merge Sort:", merge_result)

if insertion_result == merge_result:
    print("Both algorithms produced the same sorted array.")
else:
    print("The results are different.")
