def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(19))
print(is_prime(123))
print(is_prime(87))
