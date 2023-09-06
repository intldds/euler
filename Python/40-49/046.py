from math import floor, sqrt
from typing import Set


def is_prime(x: int, primes: Set[int]) -> bool:
    for p in primes:
        if x % p == 0:
            return False
    return True


def main() -> int:
    primes = set()
    x = 3
    while True:
        if is_prime(x, primes):
            primes.add(x)
        else:
            # Loop through potential values of squared number
            found = False  # Indicates if a sum was found
            y_hi = floor(sqrt((x - 3) // 2))  # Highest possible candidate for squared number of sum
            for y in range(1, y_hi+1):
                # Check whether remaining part of sum is a prime number
                if (x - 2 * y ** 2) in primes:
                    found = True
                    break
                else:
                    continue
            if not found:
                return x
        x += 2

if __name__ == '__main__':
    goldbach_breaker = main()
    print('  {}'.format(goldbach_breaker))