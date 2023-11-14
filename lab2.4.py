# Дано масив цілих чисел фіксованої довжини arr, дублюйте кожне входження нуля, зрушуючи інші елементи вправо

def duplicateZero(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 2  
        else:
            i += 1
    return arr

arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
arr2 = [1, 2, 3]

print(duplicateZero(arr1))
print(duplicateZero(arr2))