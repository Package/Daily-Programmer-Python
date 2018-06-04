from math import ceil, sqrt


def is_prime(n):
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    for x in range(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True


def gen_primes(n):
    return [2] + [x for x in range(3, n+1, 2) if is_prime(x)]


def solve(n):
    primes = gen_primes(n)
    for x in primes:
        for y in primes:
            for z in primes:
                if x + y + z == n:
                    return [x, y, z]
                
    return 'Not possible'


print(solve(111))
print(solve(17))
print(solve(199))
print(solve(287))
print(solve(53))




