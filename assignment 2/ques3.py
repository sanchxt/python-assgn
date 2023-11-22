def oddOccurrence(nums):
    count_dict = {}

    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for key, val in count_dict.items():
        if val % 2 != 0:
            return key

    return 'no such element'


num_list = [2, 3, 4, 2, 3, 4, 5, 6, 5]

print(f'list: {num_list}')
print(f'Element with odd occurrences: {oddOccurrence(num_list)}')
