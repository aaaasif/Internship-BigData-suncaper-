def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

# Test the generator (print first 10 prime numbers)
prime_gen = prime_generator()
for _ in range(120):
    print(next(prime_gen))
