# Дано масив arr цілих чисел, перевірте, чи існують два індекси i та j

def checkIndex(arr):
    num_set = set()

    for num in arr:
        if num * 2 in num_set or (num % 2 == 0 and num // 2 in num_set):
            return True

        num_set.add(num)

    return False

arr1 = [10, 2, 5, 3]
print(checkIndex(arr1))

arr2 = [3, 1, 7, 11]
print(checkIndex(arr2))
