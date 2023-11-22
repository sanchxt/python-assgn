def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def sumPrimes(start, end):
    prime_sum = 0
    for num in range(start, end + 1):
        if isPrime(num):
            prime_sum += num
    return prime_sum


start_range = int(input("Range start: "))
end_range = int(input("Range end: "))

result = sumPrimes(start_range, end_range)
print(f"Sum of prime numbers between {start_range} and {end_range}: {result}")
