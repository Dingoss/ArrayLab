# Дано масив цілих чисел nums, відсортований за неспаданням, повертає масив квадратів кожного числа, відсортованого за неспаданням

def sortedSquare(nums):
    return sorted(x*x for x in nums)

nums1 = [-4, -1, 0, 3, 10]
nums2 = [-7, -3, 2, 3, 11]

print(sortedSquare(nums1))
print(sortedSquare(nums2))


