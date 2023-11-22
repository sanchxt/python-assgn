def balParantheses(inp_string):
    stack = []
    parantheses_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in inp_string:
        if char in parantheses_map:
            top_elem = stack.pop() if stack else '#'

            if parantheses_map[char] != top_elem:
                return False
        else:
            stack.append(char)

    return not stack


inp = input('string: ')

if (balParantheses(inp)):
    print('parantheses are balanced')
else:
    print('parantheses are not balanced')
