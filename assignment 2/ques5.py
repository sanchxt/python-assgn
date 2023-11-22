def subPresent(main_str, sub_str):
    return sub_str in main_str


main_str = input('Main string: ')
sub = input('Sub string: ')

if subPresent(main_str, sub):
    print('It\'s present')
else:
    print('Not present')
