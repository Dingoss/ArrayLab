#Дано масив цілих чисел nums, перемістити всі парні цілі числа на початку масиву, а потім усі непарні цілі числа

def sortArray(nums):
    even = [x for x in nums if x % 2 == 0]  
    odd = [x for x in nums if x % 2 != 0]   
    return even + odd  

arr1 = [3, 1, 2, 4]

print(sortArray(arr1))

arr2 = [0]

print(sortArray(arr2))