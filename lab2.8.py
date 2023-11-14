# Дано масив цілих чисел arr, повертає true тоді і тільки якщо це дійсний гірський масив

def validMountainArr(arr):
    n = len(arr)

    if n < 3:
        return False

    peak = arr.index(max(arr))

    return 0 < peak < n - 1 and all(arr[i] < arr[i + 1] for i in range(peak)) and all(arr[i] > arr[i + 1] for i in range(peak, n - 1))

arr1 = [2, 1]
print(validMountainArr(arr1))

arr2 = [3, 5, 5]
print(validMountainArr(arr2))

arr3 = [0, 3, 2, 1]
print(validMountainArr(arr3))
