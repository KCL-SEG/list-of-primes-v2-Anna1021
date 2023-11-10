"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    primes_list = []
    num = 2  # Starting from the first prime number
    if number_of_primes <=0:
        raise ValueError('input number must be positive')
    while len(primes_list) < number_of_primes:
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes_list.append(num)
        num += 1

    return primes_list

# Test the function with number_of_primes = 10
result = primes(10)
print(result)



