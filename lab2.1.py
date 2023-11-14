#На вхід дається бінарний масив nums, поверніть максимальну кількість повторень 1-ці в масиві

def max_one(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


array1 = [1, 1, 0, 1, 1, 1]
array2 = [1, 0, 1, 1, 0, 1]

print(max_one(array1))
print(max_one(array2))