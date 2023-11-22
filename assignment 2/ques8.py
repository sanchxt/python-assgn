def capAlternate(str):
    res = ''

    for idx, char in enumerate(str):
        if idx % 2 == 0:
            res += char.upper()
        else:
            res += char.lower()
    return res


inp = input('string: ')

print(f'result: {capAlternate(inp)}')
