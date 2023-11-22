def filterNum(nums):
    return [num for num in nums if num % 2 == 0 and num >= 0]


num_list = [5, -2, 8, -10, 12, 16, 7, 12, -15]

print(f'Original list: {num_list}\nFiltered list: {filterNum(num_list)}')
