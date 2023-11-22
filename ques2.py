def isArmstrong(number):
    num = number
    digit_sum = 0

    while num > 0:
        digit = num % 10
        digit_sum += digit ** 3
        num //= 10

    return number == digit_sum


number = int(input('Number: '))

if isArmstrong(number):
    print('it\'s an armstrong number')
else:
    print('not an armstrong number')
