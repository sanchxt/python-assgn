def isPalindrome(inp_string):
    str = inp_string.replace(" ", "").lower()
    return str == str[::-1]


inp = input('String: ')

if (isPalindrome(inp)):
    print('It\'s a palindrome string')
else:
    print('Not palindrome')
