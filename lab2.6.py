#Маючи цілочисельний масив nums, відсортований у порядку не спадання, видаліть дублікати на місці, щоб кожен унікальний елемент 
#з’являвся лише один раз. Відносний порядок елементів має бути незмінним. Потім повертає кількість унікальних елементів у nums

def removeDuplicates(nums):
    if not nums:
        return 0  

    uniq_ptr = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[uniq_ptr]:
            uniq_ptr += 1
            nums[uniq_ptr] = nums[i]

    return uniq_ptr + 1  

nums1 = [1, 1, 2]
result1 = removeDuplicates(nums1)
print(result1, nums1[:result1])

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = removeDuplicates(nums2)
print(result2, nums2[:result2])
