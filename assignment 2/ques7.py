def subLetters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    return ', '.join(list(set1 - set2))


s1 = input('string 1: ')
s2 = input('string 2: ')

print(f'letters only in the first string: {subLetters(s1, s2)}')
