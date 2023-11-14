# Маючи масив arr, замініть кожен елемент у цьому масиві найбільшим елементом серед елементів праворуч від нього та замініть останній елемент на -1

def replaceElements(arr):
    n = len(arr)
    
    if n == 1:
        return [-1]

    max_right = -1  
    
    for i in range(n - 2, -1, -1):
        current = arr[i]  
        arr[i] = max_right  
        max_right = max(max_right, current) 

    arr[-1] = -1  

    return arr

# Приклади використання:
arr1 = [17, 18, 5, 4, 6, 1]
print(replaceElements(arr1))

arr2 = [400]
print(replaceElements(arr2))
