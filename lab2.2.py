# Дано масив nums цілих чисел, поверніть, скільки з них містять парну кількість цифр

def count_num(nums):
    def count_digits(num):
        count = 0
        while num > 0:
            num //= 10
            count += 1
        return count

    even_digits_count = 0

    for num in nums:
        digit_count = count_digits(num)
        if digit_count % 2 == 0:
            even_digits_count += 1

    return even_digits_count

nums1 = [12, 345, 2, 6, 7896]
nums2 = [555, 901, 482, 1771]

print(count_num(nums1))
print(count_num(nums2))
